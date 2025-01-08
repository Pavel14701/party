from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine  
from app.core.config import DATABASE_URL
from typing import AsyncGenerator

# Асинхронный движок для операций с базой данных
async_engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session = SessionLocal()
    try:
        yield session
    except Exception as e:
        await session.rollback()
        raise e
    finally:
        await session.close()
