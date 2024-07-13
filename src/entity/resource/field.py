from decimal import Decimal
from typing import Annotated

from pydantic import Field
from src.entity.resource.const import (
    RESOURCE_DISPLAY_NAME_MAX_LENGTH,
    RESOURCE_NAME_MAX_LENGTH,
    RESOURCE_DESCRIPTION_MAX_LENGTH,
    RESOURCE_NAME_DOC,
    RESOURCE_DESCRIPTION_DOC,
    RESOURCE_DISPLAY_NAME_DOC
)

__all__ = (
    'FieldResourceId',
    'FieldResourceName',
    'FieldResourceDisplayName',
    'FieldResourceDescription',
    'FieldResourcePrice',
    'FieldUnitId',
    'FieldUnitName'
)

FieldResourceId = Annotated[
    int,
    Field(
        title="ИД ресурса",
        ge=0
    )
]
FieldResourceDisplayName = Annotated[
    str,
    Field(
        title="Внешние имя",
        description=RESOURCE_DISPLAY_NAME_DOC,
        max_length=RESOURCE_DISPLAY_NAME_MAX_LENGTH
    )
]
FieldResourceName = Annotated[
    str,
    Field(
        title="Внутренние имя",
        description=RESOURCE_NAME_DOC,
        max_length=RESOURCE_NAME_MAX_LENGTH
    )
]
FieldResourceDescription = Annotated[
    str,
    Field(
        title=RESOURCE_DESCRIPTION_DOC,
        max_length=RESOURCE_DESCRIPTION_MAX_LENGTH
    )
]
FieldResourcePrice = Annotated[
    Decimal,
    Field(
        title="Цена"
    )
]

FieldUnitId = Annotated[
    int,
    Field(
        title="ИД Единицы измерения",
        ge=0
    )
]
FieldUnitName = Annotated[
    str,
    Field(
        title="Наименование"
    )
]
