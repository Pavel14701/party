from fastapi import HTTPException, status

from app.applications import DBSession
from app.applications.interfaces import UserAuthenticator
from app.domain.essences import Token
from app.infrastructure.models.users import User

class LoginInteractor:
    def __init__(self, db_session: DBSession, gateway: UserAuthenticator) -> None:
        self._db_session = db_session
        self._gateway = gateway

    async def __call__(self, username: str, password: str) -> Token:
        user: User = await self._gateway.authenticate(
            self._db_session, username, password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
        access_token = self._gateway.create_access_token(
            data={"sub": user.username}
        )
        return Token(access_token=access_token, token_type="bearer")
