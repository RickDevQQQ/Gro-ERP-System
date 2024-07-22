from src.api.resource.http_v1.schema import (
    CreateResourceSchema,
    ResponseResourceSchema,
    ResponseUnitSchema,
    UpdateResourceSchema
)
from src.entity.resource.dto import (
    CreateResourceDTO,
    ResourceDTO,
    UpdateResourceDTO
)


class ResourceHTTPMapper:

    @staticmethod
    def from_create_schema_to_create_dto(schema: CreateResourceSchema) -> CreateResourceDTO:
        return CreateResourceDTO(
            name=schema.name,
            display_name=schema.display_name,
            description=schema.description,
            price=schema.description,
            unit_id=schema.unit_id
        )

    @staticmethod
    def from_update_schema_to_update_dto(schema: UpdateResourceSchema) -> UpdateResourceDTO:
        return UpdateResourceDTO(
            id=schema.id,
            name=schema.name,
            display_name=schema.display_name,
            description=schema.description,
            price=schema.description,
            unit_id=schema.unit_id
        )

    @staticmethod
    def from_dto_to_response_schema(dto: ResourceDTO) -> ResponseResourceSchema:
        return ResponseResourceSchema(
            id=dto.id,
            name=dto.name,
            display_name=dto.display_name,
            description=dto.description,
            price=dto.price,
            unit=ResponseUnitSchema(
                id=dto.unit.id,
                name=dto.name,
            )
        )
