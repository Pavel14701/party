from typing import Protocol, Optional, Dict
from abc import abstractmethod
from uuid import UUID

class UUIDGenerator(Protocol):
    def __call__(self) -> UUID:
        ...

class DBSession(Protocol):
    @abstractmethod
    async def commit(self) -> None:
        ...

    @abstractmethod
    async def flush(self) -> None:
        ...

from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: str
    username: str
    hashed_password: str
    roles: List[str]

class UserAuthenticator(Protocol):
    @abstractmethod
    async def authenticate(self, username: str, password: str) -> Optional[User]:
        ...

    @abstractmethod
    async def get_current_user(self, token: str) -> Optional[User]:
        ...

    @abstractmethod
    async def create_access_token(self, data:Dict[str, str]) -> str:
        ...