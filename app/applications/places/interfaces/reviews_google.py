from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import GoogleReviewsDomainModel

class GoogleReviewSaver(Protocol):
    @abstractmethod
    async def save(self, review: GoogleReviewsDomainModel) -> None:
        ...

class GoogleReviewReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[GoogleReviewsDomainModel]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[GoogleReviewsDomainModel]:
        ...

class GoogleReviewUpdater(Protocol):
    @abstractmethod
    async def update(self, review: GoogleReviewsDomainModel) -> None:
        ...

class GoogleReviewDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...
