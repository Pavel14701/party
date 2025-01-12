from datetime import timezone
from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException, status
from jose import JWTError, jwt
from jose.exceptions import ExpiredSignatureError
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.applications.interfaces import UserAuthenticator
from app.domain.essences import User, UserInDB

class JWTAuthenticator(UserAuthenticator):
    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def authenticate(self, session: AsyncSession, username: str, password: str) -> Optional[User]:
        user = await self.get_user_by_username(session, username)
        if user and self.pwd_context.verify(password, user.password):
            return user
        return None

    async def get_current_user(self, token: str) -> Optional[User]:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            username = payload.get("sub")
            return None if username is None else UserInDB(**payload)
        except ExpiredSignatureError as e:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token expired") from e
        except JWTError as e:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token") from e

    async def get_user_by_username(self, session: AsyncSession, username: str) -> Optional[UserInDB]:
        result = await session.execute(
            text("SELECT * FROM user_users WHERE username = :username"),
            {"username": username}
        )
        return UserInDB(**row) if (row := result.fetchone()) else None

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode["exp"] = expire
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
