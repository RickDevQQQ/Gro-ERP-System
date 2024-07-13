from abc import ABC
from typing import TypeVar, TYPE_CHECKING, Generic

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.enum import SaveMethod

if TYPE_CHECKING:
    from src.core.database.model import Model

T = TypeVar('T', bound=Model)


class AbstractEntityRepository(Generic[T], ABC):
    model: T

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def save(self, method: SaveMethod) -> None:
        if method == SaveMethod.flush:
            await self.session.flush()
        elif method == SaveMethod.commit:
            await self.session.commit()
        else:
            return
