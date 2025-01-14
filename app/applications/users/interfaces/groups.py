from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain.essences import (
    UserDM, ChatDM, GroupDM,
    MessageDM, VideoDM, ImageDM,
    CuisineDM, MusicStyleDM, PlaceDM
)


class GroupSaver(Protocol):
    @abstractmethod
    async def save(self, group: GroupDM) -> None:
        ...

class GroupReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[GroupDM]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[GroupDM]:
        ...

class GroupUpdater(Protocol):
    @abstractmethod
    async def update(self, group: GroupDM) -> None:
        ...

class GroupDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...
