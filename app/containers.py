from dependency_injector import (containers, providers)
from sqlalchemy.ext.asyncio import (create_async_engine, AsyncSession)
from sqlalchemy.orm import sessionmaker
from app.core import config


class Database(containers.DeclarativeContainer):
    engine = providers.Singleton(create_async_engine, config.DATABASE_URL, echo=True)
    session = providers.Singleton(sessionmaker, bind=engine, class_=AsyncSession, expire_on_commit=False)
