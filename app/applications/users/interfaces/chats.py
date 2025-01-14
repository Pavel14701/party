from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain.essences import (
    UserDM, ChatDM, GroupDM,
    MessageDM, VideoDM, ImageDM,
    CuisineDM, MusicStyleDM, PlaceDM
)


class ChatSaver(Protocol):
    @abstractmethod
    async def save(self, chat: ChatDM) -> None:
        ...

class ChatReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> ChatDM | None:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[ChatDM]:
        ...

class ChatUpdater(Protocol):
    @abstractmethod
    async def update(self, chat: ChatDM) -> None:
        ...

class ChatDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...
