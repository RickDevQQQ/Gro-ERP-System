from typing import Annotated

from pydantic import Field

import datetime as dt

__all__ = (
    'FieldUpdateAt',
    'FieldCreatedAt',
    'FieldIsDeleted'
)

FieldCreatedAt = Annotated[
    dt.datetime,
    Field(
        title="Время создания",
    )
]
FieldUpdateAt = Annotated[
    dt.datetime,
    Field(
        title="Время обновления",
    )
]
FieldIsDeleted = Annotated[
    bool,
    Field(
        title="Является удаленным"
    )
]
