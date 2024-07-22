from sqlalchemy import false, Boolean, text, BigInteger, Integer
from sqlalchemy.orm import Mapped, mapped_column

import datetime as dt

__all__ = (
    'ColumnIsDeleted',
    'ColumnCreatedAt',
    'ColumnUpdatedAt',
    'ColumnIdAutoIncrement'
)


class ColumnIsDeleted:
    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default=false(),
        doc="Является удаленным"
    )


class ColumnUpdatedAt:
    updated_at: Mapped[dt.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=dt.datetime.now(dt.UTC),
        doc="Время обновления"
    )


class ColumnCreatedAt:
    created_at: Mapped[dt.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        doc="Время создания"
    )


class ColumnIdAutoIncrement:
    id: Mapped[BigInteger] = mapped_column(
        Integer, primary_key=True, autoincrement=True, doc="ИД записи"
    )
