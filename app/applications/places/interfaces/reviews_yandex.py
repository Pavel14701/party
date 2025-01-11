from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import YandexReviewsDomainModel

class YandexReviewSaver(Protocol):
    @abstractmethod
    async def save(self, review: YandexReviewsDomainModel) -> None:
        ...

class YandexReviewReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[YandexReviewsDomainModel]:
        ...

    @abstractmethod
    async def read_all(self) -> List[YandexReviewsDomainModel]:
        ...

class YandexReviewUpdater(Protocol):
    @abstractmethod
    async def update(self, review: YandexReviewsDomainModel) -> None:
        ...

class YandexReviewDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...
