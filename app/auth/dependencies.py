# app/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.schemas import TokenData, User
from app.auth.jwt import decode_access_token
from app.users.crud import get_user
from app.core.session import get_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_session)) -> User:
    """
    ## Получает текущего пользователя, исходя из OAuth2 токена.

    ## Аргументы:
        :class:`token (str):` OAuth2 токен, автоматически передаваемый через Depends.
        :class:`db (AsyncSession):` Асинхронная сессия базы данных, автоматически передаваемая через Depends.

    ## Возвращает:
        :class:`User:` Объект пользователя, найденного в базе данных.

    ## Исключения:
        :class:`HTTPException:` Если токен невалиден или пользователь не найден, генерируется исключение с кодом 401.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception
    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception
    token_data = TokenData(username=username)
    user = await get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user