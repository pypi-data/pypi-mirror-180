from myst.client import Client
from myst.openapi.models.time_series_get import TimeSeriesGet


def request_sync(client: Client, uuid: str) -> TimeSeriesGet:
    """Gets a time series by its unique identifier."""

    return client.request(method="get", path=f"/projects/-/time_series/{uuid}", response_class=TimeSeriesGet)
