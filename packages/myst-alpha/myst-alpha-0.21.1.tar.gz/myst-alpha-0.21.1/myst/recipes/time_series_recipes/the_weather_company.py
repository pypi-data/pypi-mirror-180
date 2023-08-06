import enum
import math
from dataclasses import dataclass
from typing import Mapping, Optional, Union

from myst.connectors.source_connectors import cleaned_observations, enhanced_forecast, historical_hourly_conditions
from myst.connectors.source_connectors.cleaned_observations import CLEANED_OBSERVATIONS_ID
from myst.connectors.source_connectors.enhanced_forecast import ENHANCED_FORECAST_ID
from myst.connectors.source_connectors.historical_hourly_conditions import HISTORICAL_HOURLY_CONDITIONS_ID
from myst.core.time.time_delta import TimeDelta
from myst.models.types import UUIDOrStr
from myst.recipes.metar_station import MetarStation
from myst.recipes.time_series_recipe import TimeSeriesRecipe
from myst.resources.layer import TimeSeriesLayer
from myst.resources.project import Project
from myst.resources.source import Source
from myst.resources.time_series import TimeSeries

_HISTORICAL_APIS_CUTOVER_BOUNDARY = TimeDelta("-PT23H")
_HISTORICAL_TO_FORECAST_CUTOVER_BOUNDARY = TimeDelta("PT1H")
_THE_WEATHER_COMPANY_DATA_SAMPLE_PERIOD = TimeDelta("PT1H")
_SOURCE_CONNECTOR_IDS = (CLEANED_OBSERVATIONS_ID, HISTORICAL_HOURLY_CONDITIONS_ID, ENHANCED_FORECAST_ID)


@dataclass
class _TWCFieldTriple:
    cleaned_observations_field: cleaned_observations.Field
    historical_hourly_conditions_field: historical_hourly_conditions.Field
    enhanced_forecast_field: enhanced_forecast.Field


@enum.unique
class Field(str, enum.Enum):
    """Data fields available from The Weather Company APIs involved in this recipe."""

    CLOUD_COVERAGE = "Cloud Coverage"
    DEW_POINT_TEMPERATURE = "Dew Point Temperature"
    RELATIVE_HUMIDITY = "Relative Humidity"
    TEMPERATURE = "Temperature"
    WIND_CHILL_TEMPERATURE = "Wind Chill Temperature"
    WIND_DIRECTION = "Wind Direction"
    WIND_SPEED = "Wind Speed"


_FIELD_MAPPINGS: Mapping[Field, _TWCFieldTriple] = {
    Field.CLOUD_COVERAGE: _TWCFieldTriple(
        cleaned_observations_field=cleaned_observations.Field.CLOUD_COVERAGE_PERCENT,
        historical_hourly_conditions_field=historical_hourly_conditions.Field.CLOUD_COVERAGE_PERCENT,
        enhanced_forecast_field=enhanced_forecast.Field.CLOUD_COVER,
    ),
    Field.DEW_POINT_TEMPERATURE: _TWCFieldTriple(
        cleaned_observations_field=cleaned_observations.Field.SURFACE_DEWPOINT_TEMPERATURE_CELSIUS,
        historical_hourly_conditions_field=historical_hourly_conditions.Field.TEMPERATURE_DEW_POINT,
        enhanced_forecast_field=enhanced_forecast.Field.TEMPERATURE_DEW_POINT,
    ),
    Field.RELATIVE_HUMIDITY: _TWCFieldTriple(
        cleaned_observations_field=cleaned_observations.Field.RELATIVE_HUMIDITY_PERCENT,
        historical_hourly_conditions_field=historical_hourly_conditions.Field.RELATIVE_HUMIDITY,
        enhanced_forecast_field=enhanced_forecast.Field.RELATIVE_HUMIDITY,
    ),
    Field.TEMPERATURE: _TWCFieldTriple(
        cleaned_observations_field=cleaned_observations.Field.SURFACE_TEMPERATURE_CELSIUS,
        historical_hourly_conditions_field=historical_hourly_conditions.Field.TEMPERATURE,
        enhanced_forecast_field=enhanced_forecast.Field.TEMPERATURE,
    ),
    Field.WIND_CHILL_TEMPERATURE: _TWCFieldTriple(
        cleaned_observations_field=cleaned_observations.Field.WIND_CHILL_TEMPERATURE_CELSIUS,
        historical_hourly_conditions_field=historical_hourly_conditions.Field.TEMPERATURE_WIND_CHILL,
        enhanced_forecast_field=enhanced_forecast.Field.TEMPERATURE_WIND_CHILL,
    ),
    Field.WIND_DIRECTION: _TWCFieldTriple(
        cleaned_observations_field=cleaned_observations.Field.WIND_DIRECTION_DEGREES,
        historical_hourly_conditions_field=historical_hourly_conditions.Field.WIND_DIRECTION,
        enhanced_forecast_field=enhanced_forecast.Field.WIND_DIRECTION,
    ),
    Field.WIND_SPEED: _TWCFieldTriple(
        cleaned_observations_field=cleaned_observations.Field.WIND_SPEED_KPH,
        historical_hourly_conditions_field=historical_hourly_conditions.Field.WIND_SPEED,
        enhanced_forecast_field=enhanced_forecast.Field.WIND_SPEED,
    ),
}


class TheWeatherCompany(TimeSeriesRecipe):
    """A recipe for creating time series that stitch together multiple The Weather Company data sources.

    This recipe is defined for a given METAR station and field. Because the three The Weather Company APIs involved in
    this recipe interpolate differently between METAR stations, we do not allow specification of arbitrary lat/long,
    which could result in a time series of poor quality. Instead, we require a particular METAR station.
    """

    def __init__(
        self, metar_station: MetarStation, field: Field, create_intermediate_time_series: bool = False
    ) -> None:
        self._metar_station = metar_station
        self._field = field
        self._create_intermediate_time_series = create_intermediate_time_series

    def create(
        self, project: Union["Project", UUIDOrStr], title: Optional[str] = None, description: Optional[str] = None
    ) -> TimeSeries:
        """Creates a new time series in the given project containing weather data for this recipe.

        This method will create the following resources in the given project:

        - A source specifying the `CleanedObservations` connector.
        - A source specifying the `HistoricalHourlyConditions` connector.
        - A source specifying the `EnhancedForecast` connector.
        - For each source, an optional intermediate time series with one layer from that source.
        - A time series with three layers:
          - One from the cleaned observations node, with no start offset and an end offset of -23 hours (exclusive)
          - One from the historical hourly conditions node, with a start offset of -23 hours (inclusive) and an
            end offset of 1 hour (exclusive)
          - One from the enhanced forecast node, with a start offset of 1 hour (inclusive) and no end offset

        When invoking this method multiple times for the same project, with recipes created for the same METAR station,
        the same sources will be reused.

        Note: when invoked with `create_intermediate_time_series=True`, the final time series's three layers link to the
        three intermediate time series nodes.

        Args:
            project: the project in which to create the time series and attendant sources
            title: the title of the time series; if none is given, will default to a combination of the field name and
                METAR station specified in the recipe
            description: the description of the time series

        Returns:
            the created time series
        """
        if not isinstance(project, Project):
            project = Project.get(project)

        latitude = self._metar_station.latitude
        longitude = self._metar_station.longitude

        # List any previously created TWC source nodes for `self._metar_station`.
        nodes = project.list_nodes()
        source_connector_nodes_by_connector_id = dict()
        for node in nodes:
            if (
                # The node must be a source node.
                isinstance(node, Source)
                # The node must be a TWC source node.
                and node.connector_uuid in _SOURCE_CONNECTOR_IDS
                # The node must use the correct latitude and longitude coordinates.
                and math.isclose(latitude, node.parameters["latitude"])
                and math.isclose(longitude, node.parameters["longitude"])
            ):
                source_connector_nodes_by_connector_id[node.connector_uuid] = node

        # Create the cleaned observations source, if it does not exist.
        if CLEANED_OBSERVATIONS_ID in source_connector_nodes_by_connector_id:
            cleaned_observations_source = source_connector_nodes_by_connector_id[CLEANED_OBSERVATIONS_ID]
        else:
            cleaned_observations_fields = [
                field_triple.cleaned_observations_field for field_triple in _FIELD_MAPPINGS.values()
            ]
            cleaned_observations_source = Source.create(
                project=project,
                title=f"CO ({self._metar_station.name})",
                connector=cleaned_observations.CleanedObservations(
                    latitude=latitude, longitude=longitude, fields=cleaned_observations_fields
                ),
            )

        # Create the historical hourly conditions source, if it does not exist.
        if HISTORICAL_HOURLY_CONDITIONS_ID in source_connector_nodes_by_connector_id:
            historical_hourly_conditions_source = source_connector_nodes_by_connector_id[
                HISTORICAL_HOURLY_CONDITIONS_ID
            ]
        else:
            historical_hourly_conditions_fields = [
                field_triple.historical_hourly_conditions_field for field_triple in _FIELD_MAPPINGS.values()
            ]
            historical_hourly_conditions_source = Source.create(
                project=project,
                title=f"HHC ({self._metar_station.name})",
                connector=historical_hourly_conditions.HistoricalHourlyConditions(
                    latitude=latitude, longitude=longitude, fields=historical_hourly_conditions_fields
                ),
            )

        # Create the enhanced forecast source, if it does not exist.
        if ENHANCED_FORECAST_ID in source_connector_nodes_by_connector_id:
            enhanced_forecast_source = source_connector_nodes_by_connector_id[ENHANCED_FORECAST_ID]
        else:
            enhanced_forecast_fields = [
                field_triple.enhanced_forecast_field for field_triple in _FIELD_MAPPINGS.values()
            ]
            enhanced_forecast_source = Source.create(
                project=project,
                title=f"EF ({self._metar_station.name})",
                connector=enhanced_forecast.EnhancedForecast(
                    latitude=latitude, longitude=longitude, fields=enhanced_forecast_fields
                ),
            )

        # Create the intermediate time series.
        if self._create_intermediate_time_series:
            co_time_series = TimeSeries.create(
                project=project,
                title=f"CO {self._field.value} ({self._metar_station.name})",
                sample_period=_THE_WEATHER_COMPANY_DATA_SAMPLE_PERIOD,
                cell_shape=(),
                coordinate_labels=(),
                axis_labels=(),
            )
            TimeSeriesLayer.create(
                project=project,
                time_series=co_time_series,
                node=cleaned_observations_source,
                order=0,
                output_index=0,
                label_indexer=_FIELD_MAPPINGS[self._field].cleaned_observations_field,
            )

            hhc_time_series = TimeSeries.create(
                project=project,
                title=f"HHC {self._field.value} ({self._metar_station.name})",
                sample_period=_THE_WEATHER_COMPANY_DATA_SAMPLE_PERIOD,
                cell_shape=(),
                coordinate_labels=(),
                axis_labels=(),
            )
            TimeSeriesLayer.create(
                project=project,
                time_series=hhc_time_series,
                node=historical_hourly_conditions_source,
                order=0,
                output_index=0,
                label_indexer=_FIELD_MAPPINGS[self._field].historical_hourly_conditions_field,
            )

            ef_time_series = TimeSeries.create(
                project=project,
                title=f"EF {self._field.value} ({self._metar_station.name})",
                sample_period=_THE_WEATHER_COMPANY_DATA_SAMPLE_PERIOD,
                cell_shape=(),
                coordinate_labels=(),
                axis_labels=(),
            )
            TimeSeriesLayer.create(
                project=project,
                time_series=ef_time_series,
                node=enhanced_forecast_source,
                order=0,
                output_index=0,
                label_indexer=_FIELD_MAPPINGS[self._field].enhanced_forecast_field,
            )

            co_upstream_node: Union[Source, TimeSeries] = co_time_series
            hhc_upstream_node: Union[Source, TimeSeries] = hhc_time_series
            ef_upstream_node: Union[Source, TimeSeries] = ef_time_series

            co_label_indexer = None
            hhc_label_indexer = None
            ef_label_indexer = None
        else:
            co_upstream_node = cleaned_observations_source
            hhc_upstream_node = historical_hourly_conditions_source
            ef_upstream_node = enhanced_forecast_source

            co_label_indexer = _FIELD_MAPPINGS[self._field].cleaned_observations_field
            hhc_label_indexer = _FIELD_MAPPINGS[self._field].historical_hourly_conditions_field
            ef_label_indexer = _FIELD_MAPPINGS[self._field].enhanced_forecast_field

        # Create the time series.
        default_title = f"{self._field.value} ({self._metar_station.name})"
        time_series = TimeSeries.create(
            project=project,
            title=title or default_title,
            sample_period=_THE_WEATHER_COMPANY_DATA_SAMPLE_PERIOD,
            cell_shape=(),
            coordinate_labels=(),
            axis_labels=(),
            description=description,
        )
        TimeSeriesLayer.create(
            project=project,
            time_series=time_series,
            node=co_upstream_node,
            order=0,
            output_index=0,
            label_indexer=co_label_indexer,
            end_timing=_HISTORICAL_APIS_CUTOVER_BOUNDARY,
        )
        TimeSeriesLayer.create(
            project=project,
            time_series=time_series,
            node=hhc_upstream_node,
            order=1,
            output_index=0,
            label_indexer=hhc_label_indexer,
            start_timing=_HISTORICAL_APIS_CUTOVER_BOUNDARY,
            end_timing=_HISTORICAL_TO_FORECAST_CUTOVER_BOUNDARY,
        )
        TimeSeriesLayer.create(
            project=project,
            time_series=time_series,
            node=ef_upstream_node,
            order=2,
            output_index=0,
            label_indexer=ef_label_indexer,
            start_timing=_HISTORICAL_TO_FORECAST_CUTOVER_BOUNDARY,
        )

        return time_series
