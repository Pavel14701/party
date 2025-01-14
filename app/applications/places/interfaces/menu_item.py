from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import MenuItemDM


class MenuItemSaver(Protocol):
    @abstractmethod
    async def save(self, menu_item: MenuItemDM) -> None:
        ...

class MenuItemReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[MenuItemDM]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[MenuItemDM]:
        ...

class MenuItemUpdater(Protocol):
    @abstractmethod
    async def update(self, menu_item: MenuItemDM) -> None:
        ...

class MenuItemDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...