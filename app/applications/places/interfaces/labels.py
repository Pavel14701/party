from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import LabelDomainModel


class LabelSaver(Protocol):
    @abstractmethod
    async def save(self, label: LabelDomainModel) -> None:
        ...

class LabelReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[LabelDomainModel]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[LabelDomainModel]:
        ...

class LabelUpdater(Protocol):
    @abstractmethod
    async def update(self, label: LabelDomainModel) -> None:
        ...

class LabelDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...