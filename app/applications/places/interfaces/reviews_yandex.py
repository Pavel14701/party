from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import YandexReviewsDM

class YandexReviewSaver(Protocol):
    @abstractmethod
    async def save(self, review: YandexReviewsDM) -> None:
        ...

class YandexReviewReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[YandexReviewsDM]:
        ...

    @abstractmethod
    async def read_all(self) -> List[YandexReviewsDM]:
        ...

class YandexReviewUpdater(Protocol):
    @abstractmethod
    async def update(self, review: YandexReviewsDM) -> None:
        ...

class YandexReviewDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...
