from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import ServiceDomainModel


class ServiceSaver(Protocol):
    @abstractmethod
    async def save(self, service: ServiceDomainModel) -> None:
        ...

class ServiceReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[ServiceDomainModel]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[ServiceDomainModel]:
        ...

class ServiceUpdater(Protocol):
    @abstractmethod
    async def update(self, service: ServiceDomainModel) -> None:
        ...

class ServiceDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...