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