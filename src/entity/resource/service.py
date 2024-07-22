from abc import ABC, abstractmethod
from typing import List

from src.core.enum import SaveMethod
from src.core.paginator import Paginator
from src.core.validation import ValidationResult
from src.entity.resource.dto import (
    CreateResourceDTO,
    UpdateResourceDTO,
    ResourceDTO, UnitDTO,
)
from src.entity.resource.repository import AbstractResourceRepository, AbstractUnitRepository
from src.entity.resource.type import (
    ResourceIdOneOrIterable,
    ResourceOneOrList,
    ResourceId, UnitId
)


class AbstractResourceService(ABC):

    @abstractmethod
    async def create(self, dto: CreateResourceDTO, *, save: SaveMethod = SaveMethod.none) -> ResourceDTO:
        ...

    @abstractmethod
    async def update(self, dto: UpdateResourceDTO, *, save: SaveMethod = SaveMethod.none) -> ResourceDTO:
        ...

    @abstractmethod
    async def delete(self, id_: ResourceId, *, save: SaveMethod = SaveMethod.none) -> None:
        ...

    @abstractmethod
    async def get_by_id(self, id_: ResourceIdOneOrIterable) -> ResourceOneOrList:
        ...

    @abstractmethod
    async def get_all(self, paginator: Paginator) -> List[ResourceDTO]:
        ...


def raise_not_found_resource():
    ValidationResult(is_valid=False, detail="Не найден ресурс").raise_for_is_valid()


def raise_not_found_unit():
    ValidationResult(is_valid=False, detail="Не найдена единица измерения").raise_for_is_valid()


class ResourceService(AbstractResourceService):

    def __init__(
        self,
        resource_repository: AbstractResourceRepository,
        unit_repository: AbstractUnitRepository
    ) -> None:
        self.resource_repository = resource_repository
        self.unit_repository = unit_repository

    async def check_exist_resource(self, id_: ResourceId) -> ResourceDTO:
        resource_dto = await self.resource_repository.get_by_id(id_)
        if resource_dto is None:
            raise_not_found_resource()
        return resource_dto

    async def check_exist_unit(self, id_: UnitId) -> UnitDTO:
        unit_dto = await self.unit_repository.get_by_id(id_)
        if unit_dto is None:
            raise_not_found_unit()
        return unit_dto

    async def create(self, dto: CreateResourceDTO, *, save: SaveMethod = SaveMethod.none) -> ResourceDTO:
        return await self.resource_repository.create(dto, save=save)

    async def update(self, dto: UpdateResourceDTO, *, save: SaveMethod = SaveMethod.none) -> ResourceDTO:
        await self.check_exist_resource(dto.id)
        await self.check_exist_unit(dto.unit_id)
        return await self.resource_repository.update(dto, save=save)

    async def delete(self, id_: ResourceId, *, save: SaveMethod = SaveMethod.none) -> None:
        await self.check_exist_resource(id_)
        return await self.resource_repository.delete(id_, save=save)

    async def get_by_id(self, id_: ResourceIdOneOrIterable) -> ResourceOneOrList:
        return await self.resource_repository.get_by_id(id_)

    async def get_all(self, paginator: Paginator) -> List[ResourceDTO]:
        return await self.resource_repository.get(paginator)
