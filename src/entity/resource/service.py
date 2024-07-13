from abc import ABC, abstractmethod
from typing import List

from src.entity.resource.dto import (
    CreateResourceDTO,
    UpdateResourceDTO,
    ResourceDTO,
)
from src.entity.resource.type import ResourceIdOneOrIterable, ResourceOneOrList, ResourceId


class AbstractResourceService(ABC):

    @abstractmethod
    def create(self, dto: CreateResourceDTO) -> ResourceDTO:
        ...

    @abstractmethod
    def update(self, dto: UpdateResourceDTO) -> ResourceDTO:
        ...

    @abstractmethod
    def delete(self, id_: ResourceId) -> None:
        ...

    @abstractmethod
    def get_by_id(self, id_: ResourceIdOneOrIterable) -> ResourceOneOrList:
        ...

    @abstractmethod
    def get_all(self) -> List[ResourceDTO]:
        ...


class ResourceService(AbstractResourceService):
    ...
