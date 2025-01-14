from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain.essences import (
    UserDM, ChatDM, GroupDM,
    MessageDM, VideoDM, ImageDM,
    CuisineDM, MusicStyleDM, PlaceDM
)

class FavoritesCuisineSaver(Protocol):
    @abstractmethod
    async def save(self, cuisine: CuisineDM) -> None:
        ...

class FavoriteCuisineReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> CuisineDM | None:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[CuisineDM]:
        ...

class FavoriteCuisineUpdater(Protocol):
    @abstractmethod
    async def update(self, cuisine: CuisineDM) -> None:
        ...

class FavoriteCuisineDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...
