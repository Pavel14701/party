from typing import Optional
from fastapi.security import OAuth2PasswordRequestForm

from app.applications import DBSession
from app.applications.auth.interfaces import UserAuthentificator
from app.domain.essences import Token
from app.infrastructure.models.users import User


class AuthentificatorInteractor:
    def __init__(self, db_session: DBSession, gateway: UserAuthentificator) -> None:
        self._gateway = gateway

    async def __call__(self, username: str, password: str) -> Optional[OAuth2PasswordRequestForm]:
        return await self._gateway.authenticate(username, password)


class CreateAccessTokenInteractor:
    def __init__(self, gateway: UserAuthentificator) -> None:
        self._gateway = gateway

    async def __call__(self, user:User) -> Token:
        return self._gateway.create_access_token(user)


class RefreshAccessTokenInteractor:
    def __init__(self, gateway: UserAuthentificator) -> None:
        self._gateway = gateway

    async def __call__(self, data) -> Token:
        return self._gateway.refresh_access_token(data)