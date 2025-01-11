from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import ImageDomainModel


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
