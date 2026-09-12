from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.core.config import settings

engine = create_async_engine(url=settings.db_url, echo=settings.db_echo)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    """Базовая модель."""

    pass


async def get_session() -> AsyncGenerator[AsyncSession]:
    """Зависимость для получения асинхронной сессии базы данных."""
    async with async_session() as session:
        yield session
