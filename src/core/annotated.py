from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.model import get_async_session

SessionAnnotated = Annotated[AsyncSession, Depends(get_async_session)]