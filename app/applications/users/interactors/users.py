from typing import Optional, List
from decimal import Decimal

from app.applications import UUIDGenerator, DBSession
from app.applications.users.interfaces import (
    UserDeleter, UserReader, UserUpdater,
    UserSaver
)
from app.applications.users.dto import (
    NewUserDTO, UpdateUserDTO, UpdateUsernameDTO
)
from app.domain import UserDM


class GetUserByIdInteractor:
    def __init__(self, gateway: UserReader) -> None:
        self._gateway = gateway

    async def __call__(self, id: str) -> Optional[UserDM]:
        return await self._gateway.read_by_id(id)


class GetUserByUsernameInteractor:
    def __init__(self, gateway: UserReader) -> None:
        self._gateway = gateway

    async def __call__(self, username: str) -> Optional[UserDM]:
        return await self._gateway.read_by_username(username)


class GetAllUsersInteractor:
    def __init__(self, gateway: UserReader) -> None:
        self._gateway = gateway

    async def __call__(self, offset:int, limit:int) -> List[UserDM]:
        return await self._gateway.read_all(offset, limit)


class NewUserInteractor:
    def __init__(
        self, db_session: DBSession, gateway: UserSaver, id_generator: UUIDGenerator
    ) -> None:
        self._db_session = db_session
        self._gateway = gateway
        self._id_generator = id_generator

    async def __call__(self, dto: NewUserDTO) -> str:
        uuid = self._id_generator()
        user_dm = UserDM(
            id=uuid,
            username=dto.username,
            firstname=dto.firstname,
            lastname=dto.lastname,
            organization=dto.organization,
            phone=dto.phone,
            email=dto.email,
            country_id=dto.country_id,
            country=dto.country,
            is_superuser=dto.is_superuser
        )
        await self._gateway.save(user_dm)
        await self._db_session.commit()
        return uuid


class UpdateUserInteractor:
    def __init__(self, db_session: DBSession, gateway: UserUpdater) -> None:
        self._db_session = db_session
        self._gateway = gateway

    async def __call__(self, dto: UpdateUserDTO) -> None:
        user=UserDM(
            id = dto.id,
            username=dto.username,
            firstname=dto.firstname,
            lastname=dto.lastname,
            phone=dto.phone,
            email=dto.email,
            country_id=dto.country_id,
            country=dto.country,
        )
        await self._gateway.update(user)
        await self._db_session.commit()


class UpdateUsernameInteractor:
    def __init__(self, db_session: DBSession, gateway: UserUpdater) -> None:
        self._db_session = db_session
        self._gateway = gateway

    async def __call__(self, dto:UpdateUsernameDTO) -> None:
        user = UserDM(
            id = dto.id,
            username = dto.username
        )
        await self._gateway.update_username(user)
        await self._db_session.commit()