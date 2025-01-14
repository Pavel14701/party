from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain.essences import (
    UserDM, ChatDM, GroupDM,
    MessageDM, VideoDM, ImageDM,
    CuisineDM, MusicStyleDM, PlaceDM
)




class ImageSaver(Protocol):
    @abstractmethod
    async def save(self, image: ImageDM) -> None:
        ...

class ImageReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[ImageDM]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[ImageDM]:
        ...

class ImageUpdater(Protocol):
    @abstractmethod
    async def update(self, image: ImageDM) -> None:
        ...

class ImageDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...
