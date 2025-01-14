from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import LabelDM


class LabelSaver(Protocol):
    @abstractmethod
    async def save(self, label: LabelDM) -> None:
        ...

class LabelReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[LabelDM]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[LabelDM]:
        ...

class LabelUpdater(Protocol):
    @abstractmethod
    async def update(self, label: LabelDM) -> None:
        ...

class LabelDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...