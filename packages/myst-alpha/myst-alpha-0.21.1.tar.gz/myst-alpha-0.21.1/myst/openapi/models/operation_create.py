from typing import Optional

from pydantic import Field
from typing_extensions import Literal

from myst.models import base_model
from myst.openapi.models.operation_create_parameters import OperationCreateParameters


class OperationCreate(base_model.BaseModel):
    """Schema for operation create requests."""

    title: str
    connector_uuid: str
    object_: Optional[Literal["Node"]] = Field("Node", alias="object")
    type: Optional[Literal["Operation"]] = "Operation"
    description: Optional[str] = None
    parameters: Optional[OperationCreateParameters] = None
