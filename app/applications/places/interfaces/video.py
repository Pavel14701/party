from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import VideoDM


class VideoSaver(Protocol):
    @abstractmethod
    async def save(self, video: VideoDM) -> None:
        ...

class VideoReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[VideoDM]:
        ...

    @abstractmethod
    async def read_all(self) -> List[VideoDM]:
        ...

class VideoUpdater(Protocol):
    @abstractmethod
    async def update(self, video: VideoDM) -> None:
        ...

class VideoDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...