from abc import abstractmethod
from typing import Iterable, List, Optional

from sqlalchemy.orm import joinedload

from src.core.enum import SaveMethod
from src.core.paginator import Paginator
from src.core.repository import AbstractEntityRepository
from src.core.type import FilterType
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
    async def get(self, paginator: Paginator) -> List[ResourceDTO]:
        ...

    @abstractmethod
    async def delete(self, id_: ResourceId, *, save: SaveMethod = SaveMethod.none) -> None:
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

    def _get_filters_from_paginator(self, paginator: Paginator) -> List[FilterType]:
        filters = []
        name = paginator.filters.get('name')
        display_name = paginator.filters.get('display_name')
        description = paginator.filters.get('description')
        if name:
            filters.append(self.model.name.ilike(f'%{name}%'))

        if display_name:
            filters.append(self.model.display_name.ilike(f'%{display_name}%'))

        if description:
            filters.append(self.model.display_name.ilike(f'%{description}%'))
        return filters

    async def get(self, paginator: Paginator) -> List[ResourceDTO]:
        filters = self._get_filters_from_paginator(paginator)
        return [
            ResourceMapper.from_model_to_dto(model)
            for model in await self.model.get_models(
                self.session,
                filters=filters,
                order_by=self.model.id.desc()
            )
        ]

    async def delete(self, id_: ResourceId, *, save: SaveMethod = SaveMethod.none) -> None:
        await self.model.update(
            self.session,
            filters=[
                self.model.id == id_
            ],
            is_deleted=True
        )
        await self.save(save)

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
