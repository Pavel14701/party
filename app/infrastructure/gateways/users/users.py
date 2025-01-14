from typing import Optional, List

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain import UserDM
from app.applications.users.interfaces.users import (
    UserSaver, UserReader, UserDeleter, UserUpdater
)

class UsersGateway(
    UserSaver, UserReader, UserDeleter, UserUpdater
):
    def __init__(self, db_session: AsyncSession):
        self._db_session = db_session

    async def get_user_by_id(self, id:str) -> Optional[UserDM]:
        query = text("SEECT * FROM user_users WHERE id = :id")
        result = await self._db_session.execute(
            statement=query,
            params={"id": id}
        )
        return UserDM(**row) if (row := result.fetchone()) else None

    async def get_user_by_username(self, username: str) -> Optional[UserDM]:
        query = text("SELECT * FROM user_users WHERE username = :username")
        result = await self._db_session.execute(
            statement=query,
            params={"username": username}
        )
        return UserDM(**row) if (row := result.fetchone()) else None

    async def read_all(self, offset: int, limit: int) -> List[UserDM]:
        query = text("SELECT * FROM user_users OFFSET :offset LIMIT :limit")
        result = await self._db_session.execute(
            statement=query,
            params={
                "offset": offset,
                "limit": limit
            }
        )
        return [UserDM(**row) for row in result.fetchall()]

    async def update(self, user) -> str:
        query = text("""
        INSERT INTO user_users
            (id, username, firstname, lastname,
            password, organization, phone, email,
            country_id, country, is_superuser)
        VALUES
            (:id, :username, :firstname, :lastname,
            :password, :organization, :phone, :email,
            :country_id, :country, :is_superuser)
        """)
        params={
            "id":user.id,
            "username":user.username,
            "firstname":user.firstname,
            "lastname": user.lastname,
            "organization": user.organization,
            "phone": user.phone_number,
            "email": user.email,
            "country_id": user.country_id,
            "country": user.country,
            "is_superuser": user.is_superuser
        }