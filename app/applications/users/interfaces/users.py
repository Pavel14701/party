from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain.essences import UserDM

class UserSaver(Protocol):
    @abstractmethod
    async def save(self, user: UserDM) -> None:
        ...

class UserReader(Protocol):
    @abstractmethod
    async def read_by_id(self, id: str) -> Optional[UserDM]:
        ...

    @abstractmethod
    async def read_by_username(self, username: str) -> Optional[UserDM]:
        ...

    @abstractmethod
    async def read_all(self) -> List[UserDM]:
        ...

class UserUpdater(Protocol):
    @abstractmethod
    async def update(self, user: UserDM) -> None:
        ...

    @abstractmethod
    async def update_username(self, user: UserDM) -> None:
        ...

class UserDeleter(Protocol):
    @abstractmethod
    async def delete(self, id: str) -> None:
        ...