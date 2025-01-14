from datetime import timezone, datetime, timedelta
from typing import Optional

from fastapi import HTTPException, status
from jose import JWTError, jwt
from jose.exceptions import ExpiredSignatureError
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.core.config import SecurityConfig
from app.applications.auth.interfaces import UserAuthentificator
from app.domain.essences import UserDM

class JWTAuthenticator(UserAuthentificator):
    def __init__(self, config: SecurityConfig, session: AsyncSession) -> None:
        self._secret_key = config.secret_key
        self._algorithm = config.algorithm
        self._db_session = session
        self._token_expire = config.access_token_expire_minutes
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def authenticate(self, username: str, password: str) -> Optional[UserDM]:
        user = await self.get_user_by_username(username)
        if user and self._pwd_context.verify(password, user.password):
            return user
        return None

    async def get_current_user(self, token: str) -> Optional[UserDM]:
        try:
            payload = jwt.decode(token, self._secret_key, algorithms=[self._algorithm])
            username = payload.get("sub")
            return None if username is None else UserDM(**payload)
        except ExpiredSignatureError as e:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token expired") from e
        except JWTError as e:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token") from e



    def create_access_token(self, data: dict):
        to_encode = data.copy()
        to_encode["exp"] = datetime.now(timezone.utc) + self._token_expire
        return jwt.encode(
            to_encode, self._secret_key, algorithm=self._algorithm
        )

    def refresh(self, token: str) -> str:
        try:
            payload = jwt.decode(token, self._secret_key, algorithms=[self._algorithm], options={"verify_exp": False})
            if username := payload.get("sub"):
                return self.create_access_token(
                    {"sub": username}
                )
            else:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")
        except JWTError as e:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token") from e
