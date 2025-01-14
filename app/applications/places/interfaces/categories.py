from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import CategoryDM


class CategorySaver(Protocol):
    @abstractmethod
    async def save(self, category: CategoryDM) -> None:
        ...

class CategoryReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[CategoryDM]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[CategoryDM]:
        ...

class CategoryUpdater(Protocol):
    @abstractmethod
    async def update(self, category: CategoryDM) -> None:
        ...

class CategoryDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...
