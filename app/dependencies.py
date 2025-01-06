from sqlalchemy.ext.asyncio import AsyncSession
from .containers import Database
from typing import AsyncGenerator

database = Database()

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with database.session() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()