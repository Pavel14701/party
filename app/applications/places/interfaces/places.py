from abc import abstractmethod
from typing import Protocol
from typing import List, Optional
from decimal import Decimal

from app.domain import PlaceDM

class PlaceSaver(Protocol):
    @abstractmethod
    async def save(self, place: PlaceDM) -> None:
        ...

class PlaceReader(Protocol):
    @abstractmethod
    async def read_by_id(self, id: str) -> Optional[PlaceDM]:
        ...

    @abstractmethod
    async def read_all(self, offset: int, limit: int) -> List[PlaceDM]:
        ...

    @abstractmethod
    async def read_by_name(self, name: str) -> Optional[PlaceDM]:
        ...

    @abstractmethod
    async def read_near_geo(self, latitude:Decimal, longtitude:Decimal, radius:Decimal) -> Optional[List[PlaceDM]]:
        ...

    @abstractmethod
    async def read_near_geo_by_id(self, id:str, radius: Decimal) -> Optional[List[PlaceDM]]:
        ...

class PlaceUpdater(Protocol):
    @abstractmethod
    async def update(self, id: Optional[str], name: Optional[str], place: PlaceDM) -> None:
        ...

class PlaceGeoUpdater(Protocol):
    @abstractmethod
    async def update_geo(self, id: Optional[str], name: Optional[str], place: PlaceDM) -> None:
        ...

class PlaceNameUpdater(Protocol):
    @abstractmethod
    async def update_name(self, id: str, place: PlaceDM) -> None:
        ...

class PlaceDescriptionUpdater(Protocol):
    @abstractmethod
    async def update_description(self, id: Optional[str], name:Optional[str], place: PlaceDM) -> None:
        ...

class PlaceLogoUpdater(Protocol):
    @abstractmethod
    async def update_logo(self, id: Optional[str], name: Optional[str], place: PlaceDM) -> None:
        ...

class PlaceDeleter(Protocol):
    @abstractmethod
    async def delete(self, id: Optional[str], name: Optional[str]) -> None:
        ...