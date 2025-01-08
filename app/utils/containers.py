from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core import config
from typing import AsyncGenerator

class Database(containers.DeclarativeContainer):
    """## Контейнер зависимостей для управления подключением к базе данных."""
    engine = providers.Singleton(create_async_engine, config.DATABASE_URL, echo=True)
    SessionLocal = providers.Singleton(sessionmaker, bind=engine, class_=AsyncSession, expire_on_commit=False)

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """## Получает асинхронную сессию базы данных.
        ## Возвращает:
            :class:`AsyncGenerator[AsyncSession, None]:` Генератор асинхронной сессии базы данных.
        """
        session: AsyncSession = self.SessionLocal()
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()
