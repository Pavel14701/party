from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import OrganizationDM

class OrganizationSaver(Protocol):
    @abstractmethod
    async def save(self, organization: OrganizationDM) -> None:
        ...

class OrganizationReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[OrganizationDM]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[OrganizationDM]:
        ...

class OrganizationUpdater(Protocol):
    @abstractmethod
    async def update(self, organization: OrganizationDM) -> None:
        ...

class OrganizationDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...