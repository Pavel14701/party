from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain.essences import (
    UserDM, ChatDM, GroupDM,
    MessageDM, VideoDM, ImageDM,
    CuisineDM, MusicStyleDM, PlaceDM
)


class MessageSaver(Protocol):
    @abstractmethod
    async def save(self, message: MessageDM) -> None:
        ...

class MessageReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> MessageDM | None:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[MessageDM]:
        ...

class MessageUpdater(Protocol):
    @abstractmethod
    async def update(self, message: MessageDM) -> None:
        ...

class MessageDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...
