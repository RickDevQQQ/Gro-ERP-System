from src.entity.resource.dto import ResourceDTO, UnitDTO
from src.entity.resource.model import Resource


class ResourceMapper:

    @staticmethod
    def from_model_to_dto(model: Resource) -> ResourceDTO:
        return ResourceDTO(
            id=model.id,
            name=model.name,
            display_name=model.display_name,
            description=model.description,
            price=model.price,
            created_at=model.created_at,
            unit=UnitDTO(
                id=model.unit.id,
                name=model.unit.name
            )
        )
