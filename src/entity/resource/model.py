from sqlalchemy import String, DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database.model import Model
from src.core.database.column import ColumnIsDeleted, ColumnCreatedAt, ColumnIdAutoIncrement
from src.entity.resource.const import (
    RESOURCE_DISPLAY_NAME_MAX_LENGTH,
    RESOURCE_DESCRIPTION_MAX_LENGTH,
    RESOURCE_NAME_MAX_LENGTH,
    RESOURCE_NAME_DOC,
    RESOURCE_DESCRIPTION_DOC,
    RESOURCE_DISPLAY_NAME_DOC
)

from decimal import Decimal

__all__ = (
    'Resource',
    "Unit"
)


class Resource(ColumnIdAutoIncrement, ColumnCreatedAt, ColumnIsDeleted, Model):

    display_name: Mapped[str] = mapped_column(
        String(RESOURCE_DISPLAY_NAME_MAX_LENGTH), doc=RESOURCE_DISPLAY_NAME_DOC
    )
    name: Mapped[str] = mapped_column(
        String(RESOURCE_NAME_MAX_LENGTH), doc=RESOURCE_NAME_DOC
    )
    description: Mapped[str] = mapped_column(
        String(RESOURCE_DESCRIPTION_MAX_LENGTH), doc=RESOURCE_DESCRIPTION_DOC
    )
    price: Mapped[Decimal] = mapped_column(
        DECIMAL(precision=12, scale=2, decimal_return_scale=2, asdecimal=True), doc="Цена"
    )
    unit_id: Mapped[int] = mapped_column(
        ForeignKey("unit.id"), doc="ИД Единицы измерения"
    )

    unit: Mapped['Unit'] = relationship('Unit')


class Unit(ColumnIdAutoIncrement, Model):
    name: Mapped[str] = mapped_column(String(128), doc="Наименование")
