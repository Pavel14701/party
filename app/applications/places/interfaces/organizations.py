from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import OrganizationDomainModel

class OrganizationSaver(Protocol):
    @abstractmethod
    async def save(self, organization: OrganizationDomainModel) -> None:
        ...

class OrganizationReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Optional[OrganizationDomainModel]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[OrganizationDomainModel]:
        ...

class OrganizationUpdater(Protocol):
    @abstractmethod
    async def update(self, organization: OrganizationDomainModel) -> None:
        ...

class OrganizationDeleter(Protocol):
    @abstractmethod
    async def delete(self, uuid: str) -> None:
        ...