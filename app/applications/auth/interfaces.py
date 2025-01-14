from typing import Protocol, Optional, Dict
from abc import abstractmethod

from fastapi.security import OAuth2PasswordRequestForm

from app.domain.essences import Token


class UserAuthentificator(Protocol):
    @abstractmethod
    async def authenticate(self, username: str, password: str) -> Optional[OAuth2PasswordRequestForm]:
        ...

    @abstractmethod
    async def create_access_token(self, data:Dict[str, str]) -> str:
        ...

    @abstractmethod
    async def refresh_access_token(self, data:Dict[str,str]) -> str:
        ...