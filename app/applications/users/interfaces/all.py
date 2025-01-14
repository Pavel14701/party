from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain.essences import (
    UserDM, ChatDM, GroupDM,
    MessageDM, VideoDM, ImageDM,
    CuisineDM, MusicStyleDM, PlaceDM
)


class FavoriteMusicStyleSaver(Protocol):
    @abstractmethod
    async def save(self, music_style: MusicStyleDM) -> None:
        ...

class FavoriteMusicStyleReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[MusicStyleDM]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[MusicStyleDM]:
        ...

class FavoriteMusicStyleUpdater(Protocol):
    @abstractmethod
    async def update(self, music_style: MusicStyleDM) -> None:
        ...

class FavoriteMusicStyleDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...

class FavoritePlaceSaver(Protocol):
    @abstractmethod
    async def save(self, place: PlaceDM) -> None:
        ...

class FavoritePlaceReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[PlaceDM]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[PlaceDM]:
        ...

class FavoritePlaceUpdater(Protocol):
    @abstractmethod
    async def update(self, place: PlaceDM) -> None:
        ...

class FavoritePlaceDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...
