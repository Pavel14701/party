from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from app.core.config import DatabaseConfig


def new_session_maker(psql_config: DatabaseConfig) -> async_sessionmaker[AsyncSession]:
    database_uri = "postgresql+asyncpg://{username}:{password}@{host}:{port}/{database}".format(
        username=psql_config.username,
        password=psql_config.password,
        host=psql_config.host,
        port=psql_config.port,
        database=psql_config.database,
    )

    engine = create_async_engine(
        database_uri,
        pool_size=15,
        max_overflow=15,
        connect_args={
            "connect_timeout": 5,
        },
    )
    return async_sessionmaker(engine, class_=AsyncSession, autoflush=False, expire_on_commit=False)