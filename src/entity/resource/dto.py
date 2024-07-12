from pydantic import BaseModel

from src.core.field import (
    FieldCreatedAt,
)
from src.entity.resource.field import (
    FieldResourceName,
    FieldResourceDescription,
    FieldResourceDisplayName,
    FieldResourceId
)


class CreateResourceDTO(BaseModel):
    display_name: FieldResourceDisplayName
    name: FieldResourceName
    description: FieldResourceDescription


class UpdateResourceDTO(CreateResourceDTO):
    id: FieldResourceId


class ResourceDTO(UpdateResourceDTO):
    created_at: FieldCreatedAt
