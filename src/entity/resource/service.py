from abc import ABC, abstractmethod
from typing import List

from src.core.enum import SaveMethod
from src.core.paginator import Paginator
from src.entity.resource.dto import (
    CreateResourceDTO,
    UpdateResourceDTO,
    ResourceDTO,
)
from src.entity.resource.repository import AbstractResourceRepository
from src.entity.resource.type import (
    ResourceIdOneOrIterable,
    ResourceOneOrList,
    ResourceId
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


class ResourceService(AbstractResourceService):

    def __init__(self, resource_repository: AbstractResourceRepository) -> None:
        self.resource_repository = resource_repository

    async def create(self, dto: CreateResourceDTO, *, save: SaveMethod = SaveMethod.none) -> ResourceDTO:
        return await self.resource_repository.create(dto, save)

    async def update(self, dto: UpdateResourceDTO, *, save: SaveMethod = SaveMethod.none) -> ResourceDTO:
        return await self.resource_repository.update(dto, save)

    async def delete(self, id_: ResourceId, *, save: SaveMethod = SaveMethod.none) -> None:
        return await self.resource_repository.delete(id_, save)

    async def get_by_id(self, id_: ResourceIdOneOrIterable) -> ResourceOneOrList:
        return await self.resource_repository.get_by_id(id_)

    async def get_all(self, paginator: Paginator) -> List[ResourceDTO]:
        return await self.resource_repository.get(paginator)
