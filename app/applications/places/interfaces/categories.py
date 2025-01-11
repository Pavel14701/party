from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import CategoryDomainModel


class CategorySaver(Protocol):
    @abstractmethod
    async def save(self, category: CategoryDomainModel) -> None:
        ...

class CategoryReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[CategoryDomainModel]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[CategoryDomainModel]:
        ...

class CategoryUpdater(Protocol):
    @abstractmethod
    async def update(self, category: CategoryDomainModel) -> None:
        ...

class CategoryDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...
