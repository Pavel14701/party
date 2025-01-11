from abc import abstractmethod
from typing import Protocol
from uuid import UUID
from datetime import datetime
from typing import List, Optional

from app.domain.essences import (
    UserDomainModel, ChatDomainModel, GroupDomainModel,
    MessageDomainModel, VideoDomainModel, ImageDomainModel,
    CuisineDomainModel, MusicStyleDomainModel, PlaceDM
)

class UserSaver(Protocol):
    @abstractmethod
    async def save(self, user: UserDomainModel) -> None:
        ...

class UserReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[UserDomainModel]:
        ...

    @abstractmethod
    async def read_by_username(self, username: str) -> Optional[UserDomainModel]:
        ...

    @abstractmethod
    async def read_all(self) -> List[UserDomainModel]:
        ...

class UserUpdater(Protocol):
    @abstractmethod
    async def update(self, user: UserDomainModel) -> None:
        ...

class UserDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...

class ChatSaver(Protocol):
    @abstractmethod
    async def save(self, chat: ChatDomainModel) -> None:
        ...

class ChatReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> ChatDomainModel | None:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[ChatDomainModel]:
        ...

class ChatUpdater(Protocol):
    @abstractmethod
    async def update(self, chat: ChatDomainModel) -> None:
        ...

class ChatDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...

class GroupSaver(Protocol):
    @abstractmethod
    async def save(self, group: GroupDomainModel) -> None:
        ...

class GroupReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[GroupDomainModel]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[GroupDomainModel]:
        ...

class GroupUpdater(Protocol):
    @abstractmethod
    async def update(self, group: GroupDomainModel) -> None:
        ...

class GroupDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...

class MessageSaver(Protocol):
    @abstractmethod
    async def save(self, message: MessageDomainModel) -> None:
        ...

class MessageReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> MessageDomainModel | None:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[MessageDomainModel]:
        ...

class MessageUpdater(Protocol):
    @abstractmethod
    async def update(self, message: MessageDomainModel) -> None:
        ...

class MessageDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...

class VideoSaver(Protocol):
    @abstractmethod
    async def save(self, video: VideoDomainModel) -> None:
        ...

class VideoReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[VideoDomainModel]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[VideoDomainModel]:
        ...

class VideoUpdater(Protocol):
    @abstractmethod
    async def update(self, video: VideoDomainModel) -> None:
        ...

class VideoDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...

class ImageSaver(Protocol):
    @abstractmethod
    async def save(self, image: ImageDomainModel) -> None:
        ...

class ImageReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[ImageDomainModel]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[ImageDomainModel]:
        ...

class ImageUpdater(Protocol):
    @abstractmethod
    async def update(self, image: ImageDomainModel) -> None:
        ...

class ImageDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...

class CuisineSaver(Protocol):
    @abstractmethod
    async def save(self, cuisine: CuisineDomainModel) -> None:
        ...

class CuisineReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> CuisineDomainModel | None:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[CuisineDomainModel]:
        ...

class CuisineUpdater(Protocol):
    @abstractmethod
    async def update(self, cuisine: CuisineDomainModel) -> None:
        ...

class CuisineDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...

class MusicStyleSaver(Protocol):
    @abstractmethod
    async def save(self, music_style: MusicStyleDomainModel) -> None:
        ...

class MusicStyleReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[MusicStyleDomainModel]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[MusicStyleDomainModel]:
        ...

class MusicStyleUpdater(Protocol):
    @abstractmethod
    async def update(self, music_style: MusicStyleDomainModel) -> None:
        ...

class MusicStyleDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...

class PlaceSaver(Protocol):
    @abstractmethod
    async def save(self, place: PlaceDM) -> None:
        ...

class PlaceReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[PlaceDM]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[PlaceDM]:
        ...

class PlaceUpdater(Protocol):
    @abstractmethod
    async def update(self, place: PlaceDM) -> None:
        ...

class PlaceDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...
