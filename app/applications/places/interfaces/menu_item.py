from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import MenuItemDomainModel


class MenuItemSaver(Protocol):
    @abstractmethod
    async def save(self, menu_item: MenuItemDomainModel) -> None:
        ...

class MenuItemReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[MenuItemDomainModel]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[MenuItemDomainModel]:
        ...

class MenuItemUpdater(Protocol):
    @abstractmethod
    async def update(self, menu_item: MenuItemDomainModel) -> None:
        ...

class MenuItemDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...