# app/routers/auth.py
from fastapi import (
    APIRouter, Depends, HTTPException,
    status
)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.schemas import Token
from app.auth.security import verify_password
from app.auth.jwt import create_access_token
from app.infrastructure.database import get_session
from app.users.crud import get_user

router = APIRouter()

@router.post("/token", response_model=Token)
async def login_for_access_token(db: AsyncSession = Depends(get_session), form_data: OAuth2PasswordRequestForm = Depends()):
    user = await get_user(db, username=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
