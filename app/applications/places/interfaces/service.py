from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import ServiceDM


class ServiceSaver(Protocol):
    @abstractmethod
    async def save(self, service: ServiceDM) -> None:
        ...

class ServiceReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[ServiceDM]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[ServiceDM]:
        ...

class ServiceUpdater(Protocol):
    @abstractmethod
    async def update(self, service: ServiceDM) -> None:
        ...

class ServiceDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...