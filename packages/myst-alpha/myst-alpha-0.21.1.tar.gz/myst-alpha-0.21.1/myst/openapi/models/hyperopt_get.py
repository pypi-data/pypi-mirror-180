from typing import Optional

from pydantic import Field
from typing_extensions import Literal

from myst.models import base_model
from myst.openapi.models.hpo_metric import HPOMetric


class HyperoptGet(base_model.BaseModel):
    """Hyperopt search algorithm schema for get responses.

    See https://hyperopt.github.io/hyperopt/ for `hyperopt` reference."""

    metric: HPOMetric
    num_trials: int
    max_concurrent_trials: int
    algorithm: Literal["TPE"]
    n_startup_jobs: int
    object_: Optional[Literal["SearchAlgorithm"]] = Field(..., alias="object")
    type: Optional[Literal["Hyperopt"]] = "Hyperopt"
