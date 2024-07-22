from typing import List

from fastapi import APIRouter, status, Depends

from src.api.resource.http_v1.mapper import ResourceHTTPMapper
from src.api.resource.http_v1.schema import (
    CreateResourceSchema,
    ResponseResourceSchema,
    UpdateResourceSchema
)
from src.core.annotated import SessionAnnotated
from src.core.enum import SaveMethod
from src.core.paginator import PaginatorInfoAnnotated, Paginator
from src.entity.resource.repository import ResourceRepository, UnitRepository
from src.entity.resource.service import ResourceService

api_resource_router = APIRouter(
    prefix='/api/v1/resource'
)


def get_paginator_for_order(
    info: PaginatorInfoAnnotated
):
    return Paginator(limit=info[0], page=info[1])


@api_resource_router.post(
    '/',
    summary="Создать Ресурс",
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseResourceSchema
)
async def create(
    schema: CreateResourceSchema,
    session: SessionAnnotated
):
    service = ResourceService(
        resource_repository=ResourceRepository(session),
        unit_repository=UnitRepository(session)
    )
    create_dto = ResourceHTTPMapper.from_create_schema_to_create_dto(schema)

    resource_dto = await service.create(create_dto, save=SaveMethod.commit)

    response_schema = ResourceHTTPMapper.from_dto_to_response_schema(resource_dto)

    return response_schema


@api_resource_router.put(
    '/',
    summary="Обновить Ресурс",
    response_model=ResponseResourceSchema
)
async def update(
    schema: UpdateResourceSchema,
    session: SessionAnnotated
):
    service = ResourceService(
        resource_repository=ResourceRepository(session),
        unit_repository=UnitRepository(session)
    )

    update_dto = ResourceHTTPMapper.from_update_schema_to_update_dto(schema)

    resource_dto = await service.update(update_dto, save=SaveMethod.commit)

    response_schema = ResourceHTTPMapper.from_dto_to_response_schema(resource_dto)

    return response_schema


@api_resource_router.delete(
    '/{resource_id}/',
    summary="Удалить Ресурс",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete(
    resource_id: int,
    session: SessionAnnotated
):
    service = ResourceService(
        resource_repository=ResourceRepository(session),
        unit_repository=UnitRepository(session)
    )

    await service.delete(resource_id, save=SaveMethod.commit)


@api_resource_router.get(
    '/{resource_id}/',
    summary="Получить ресурс",
    response_model=ResponseResourceSchema
)
async def get_by_id(
    session: SessionAnnotated,
    resource_id: int
):
    service = ResourceService(
        resource_repository=ResourceRepository(session),
        unit_repository=UnitRepository(session)
    )

    resources_dto = await service.get_by_id(resource_id)

    return ResourceHTTPMapper.from_dto_to_response_schema(resources_dto)


@api_resource_router.get(
    '/',
    summary="Получить все ресурсы",
    response_model=List[ResponseResourceSchema]
)
async def get(
    session: SessionAnnotated,
    paginator: Paginator = Depends(get_paginator_for_order)
):
    service = ResourceService(
        resource_repository=ResourceRepository(session),
        unit_repository=UnitRepository(session)
    )

    resources_dto = await service.get_all(paginator)

    return [
        ResourceHTTPMapper.from_dto_to_response_schema(dto)
        for dto in resources_dto
    ]
