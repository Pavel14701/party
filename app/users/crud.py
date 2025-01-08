# app/crud/users.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.users.models import User
from app.auth.schemas import UserInDB
from app.users.schemas import UserCreate
from app.auth.security import get_password_hash
from typing import Optional

async def get_user(db: AsyncSession, username: str) -> Optional[UserInDB]:
    result = await db.execute(select(User).filter(User.username == username))
    if user := result.scalars().first():
        return UserInDB(**user.__dict__)
    return None

async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    user = User(
        username=user_in.username,
        email=user_in.email,
        password=get_password_hash(user_in.password)
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

