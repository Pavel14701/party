from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import MenuCategoryDomainModel


class MenuCategorySaver(Protocol):
    @abstractmethod
    async def save(self, menu_category: MenuCategoryDomainModel) -> None:
        ...

class MenuCategoryReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[MenuCategoryDomainModel]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[MenuCategoryDomainModel]:
        ...

class MenuCategoryUpdater(Protocol):
    @abstractmethod
    async def update(self, menu_category: MenuCategoryDomainModel) -> None:
        ...

class MenuCategoryDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...
