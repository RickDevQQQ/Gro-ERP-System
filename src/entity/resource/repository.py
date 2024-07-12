from abc import abstractmethod

from src.core.repository import AbstractRepository
from src.entity.resource.dto import CreateResourceDTO, ResourceDTO, UpdateResourceDTO
from src.entity.resource.type import ResourceIdOneOrIterable, ResourceOneOrList


class AbstractResourceRepository(AbstractRepository):

    @abstractmethod
    async def get_by_id(self, id_: ResourceIdOneOrIterable) -> ResourceOneOrList:
        pass

    @abstractmethod
    async def create(self, dto: CreateResourceDTO) -> ResourceDTO:
        ...

    @abstractmethod
    async def update(self, dto: UpdateResourceDTO) -> ResourceDTO:
        ...


