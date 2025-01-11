from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import VideoDomainModel


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