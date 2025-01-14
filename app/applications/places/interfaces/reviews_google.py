from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import GoogleReviewsDM

class GoogleReviewSaver(Protocol):
    @abstractmethod
    async def save(self, review: GoogleReviewsDM) -> None:
        ...

class GoogleReviewReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[GoogleReviewsDM]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[GoogleReviewsDM]:
        ...

class GoogleReviewUpdater(Protocol):
    @abstractmethod
    async def update(self, review: GoogleReviewsDM) -> None:
        ...

class GoogleReviewDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...
