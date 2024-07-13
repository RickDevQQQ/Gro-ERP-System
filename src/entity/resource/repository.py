from abc import abstractmethod
from typing import Iterable, List, Optional

from sqlalchemy.orm import joinedload

from src.core.enum import SaveMethod
from src.core.repository import AbstractEntityRepository
from src.entity.resource.dto import CreateResourceDTO, ResourceDTO, UpdateResourceDTO
from src.entity.resource.mapper import ResourceMapper
from src.entity.resource.model import Resource
from src.entity.resource.type import ResourceIdOneOrIterable, ResourceOneOrList, ResourceId


class AbstractResourceRepository(AbstractEntityRepository):
    model = Resource

    @abstractmethod
    async def get_by_id(self, id_: ResourceIdOneOrIterable) -> ResourceOneOrList:
        ...

    @abstractmethod
    async def create(self, dto: CreateResourceDTO, *, save: SaveMethod = SaveMethod.none) -> ResourceDTO:
        ...

    @abstractmethod
    async def update(self, dto: UpdateResourceDTO, *, save: SaveMethod = SaveMethod.none) -> ResourceDTO:
        ...


class ResourceRepository(AbstractResourceRepository):

    async def _get_by_ids(self, id_: Iterable[ResourceId]) -> List[Resource]:
        return await self.model.get_models(
            self.session,
            filters=[
                self.model.id.in_(id_)
            ],
            load_options=[
                joinedload(self.model.unit)
            ]
        )

    async def _get_by_id(self, id_: ResourceId) -> Optional[Resource]:
        return await self.model.get_models(
            self.session,
            filters=[
                self.model.id == id_,
            ],
            load_options=[
                joinedload(self.model.unit)
            ],
            first=True
        )

    async def get_by_id(self, id_: ResourceIdOneOrIterable) -> ResourceOneOrList:
        if isinstance(id_, int):
            model = await self._get_by_id(id_)
            if model is None:
                return
            return ResourceMapper.from_model_to_dto(model)
        return [
            ResourceMapper.from_model_to_dto(model)
            for model in await self._get_by_ids(id_)
        ]

    async def get(self) -> List[ResourceDTO]:
        ...

    async def create(self, dto: CreateResourceDTO, *, save: SaveMethod = SaveMethod.none) -> ResourceDTO:
        model = Resource(
            display_name=dto.display_name,
            name=dto.name,
            description=dto.description,
            price=dto.price,
            unit_id=dto.unit_id
        )
        await self.save(save)
        return ResourceMapper.from_model_to_dto(model)

    async def update(self, dto: UpdateResourceDTO, *, save: SaveMethod = SaveMethod.none) -> None:
        await self.model.update(
            self.session,
            filters=[
                self.model.id == dto.id
            ],
            display_name=dto.display_name,
            name=dto.name,
            description=dto.description,
            price=dto.description,
            unit_id=dto.unit_id
        )
        await self.save(save)
