from abc import abstractmethod
from typing import Protocol
from typing import List, Optional

from app.domain import PlaceHoursDM


class PlaceHoursSaver(Protocol):
    @abstractmethod
    async def save(self, place_hours: PlaceHoursDM) -> None:
        ...

class PlaceHoursReader(Protocol):
    @abstractmethod
    async def read_by_id(self, id: str) -> Optional[PlaceHoursDM]:
        ...
    
    @abstractmethod
    async def read_all(self) -> List[PlaceHoursDM]:
        ...

class PlaceHoursUpdater(Protocol):
    @abstractmethod
    async def update(self, place_hours: PlaceHoursDM) -> None:
        ...

class PlaceHoursDeleter(Protocol):
    @abstractmethod
    async def delete(self, id: str) -> None:
        ...