from typing import List

from pydantic import Field
from typing_extensions import Literal

from myst.models import base_model
from myst.openapi.models.hpo_metric import HPOMetric
from myst.openapi.models.hpo_trial import HPOTrial


class HPOResultGet(base_model.BaseModel):
    """Schema for model fit result get responses."""

    object_: Literal["HPOResult"] = Field(..., alias="object")
    uuid: str
    create_time: str
    metric: HPOMetric
    best_trial: HPOTrial
    trials: List[HPOTrial]
