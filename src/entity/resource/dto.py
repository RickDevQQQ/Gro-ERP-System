from pydantic import BaseModel

from src.core.field import (
    FieldCreatedAt,
)
from src.entity.resource.field import (
    FieldResourceName,
    FieldResourceDescription,
    FieldResourceDisplayName,
    FieldResourcePrice,

    FieldResourceId,
    FieldUnitId,
    FieldUnitName
)


class CreateResourceDTO(BaseModel):
    display_name: FieldResourceDisplayName
    name: FieldResourceName
    description: FieldResourceDescription
    price: FieldResourcePrice
    unit_id: FieldUnitId


class UpdateResourceDTO(CreateResourceDTO):
    id: FieldResourceId


class UnitDTO(BaseModel):
    id: FieldUnitId
    name: FieldUnitName


class ResourceDTO(BaseModel):
    id: FieldResourceId
    display_name: FieldResourceDisplayName
    name: FieldResourceName
    description: FieldResourceDescription
    price: FieldResourcePrice
    created_at: FieldCreatedAt
    unit: UnitDTO
