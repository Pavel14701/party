from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.schemas import TokenData, User, UserInDB
from app.auth.security import verify_password, get_password_hash
from app.auth.jwt import create_access_token
from app.core.session import get_session
from app.users.crud import get_user

router = APIRouter()

@router.post("/token")
async def login_for_access_token(db: AsyncSession = Depends(get_session), form_data: OAuth2PasswordRequestForm = Depends()):
    """
    ## Аутентифицирует пользователя и выдает токен доступа.
    ## Аргументы:
        :class:`db (AsyncSession):` Асинхронная сессия базы данных, автоматически передаваемая через Depends.
        :class:`form_data (OAuth2PasswordRequestForm):` Данные формы для аутентификации пользователя, автоматически передаваемые через Depends.
    ## Возвращает:
        :class:`dict:` Словарь с токеном доступа и типом токена.
    ## Исключения:
        :class:`HTTPException:` Если имя пользователя или пароль неверны, генерируется исключение с кодом 401.
    """
    user = await get_user(db, username=form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


