from pydantic import BaseModel
from src.entity.resource.field import (
    FieldResourceId,
    FieldResourceName,
    FieldResourceDescription,
    FieldResourceDisplayName,
    FieldResourcePrice,
    FieldUnitId,
    FieldUnitName
)


class CreateResourceSchema(BaseModel):
    name: FieldResourceName
    display_name: FieldResourceDisplayName
    description: FieldResourceDescription
    price: FieldResourcePrice
    unit_id: FieldUnitId


class UpdateResourceSchema(CreateResourceSchema):
    id: FieldResourceId


class ResponseUnitSchema(BaseModel):
    id: FieldUnitId
    name: FieldUnitName


class ResponseResourceSchema(BaseModel):
    id: FieldResourceId
    name: FieldResourceName
    display_name: FieldResourceDisplayName
    description: FieldResourceDescription
    price: FieldResourcePrice
    unit: ResponseUnitSchema
