from typing import Optional, List
from decimal import Decimal

from app.applications import UUIDGenerator, DBSession
from app.applications.places.interfaces import (
    PlaceReader, PlaceSaver,
    PlaceUpdater, PlaceDeleter,
    PlaceGeoUpdater, PlaceDescriptionUpdater, 
    PlaceLogoUpdater, PlaceNameUpdater
)
from app.applications.places.dto import (
    NewPlaceDTO, UpdatePlaceDTO,
    UpdateGeoPlaceDTO, UpdateDescriptionPlaceDTO,
    UpdateLogoPlaceDTO, UpdateNamePlaceDTO
) 
from app.domain import PlaceDM


class GetPlaceByIdInteractor:
    def __init__(self, gateway: PlaceReader) -> None:
        self._gateway = gateway

    async def __call__(self, id: str) -> Optional[PlaceDM]:
        return await self._gateway.read_by_id(id)


class GetPlaceByNameInteractor:
    def __init__(self, gateway: PlaceReader) -> None:
        self._gateway = gateway

    async def __call__(self, name: str) -> Optional[List[PlaceDM]]:
        return await self._gateway.read_by_name(name)


class GetPlaceByGeoInteractor:
    def __init__(self, gateway: PlaceReader) -> None:
        self._gateway = gateway

    async def __call__(
        self, latitude: Decimal, longitude: Decimal, radius: Decimal
    ) -> Optional[List[PlaceDM]]:
        return await self._gateway.read_near_geo(latitude, longitude, radius)


class GetPlaceByIdGeoInteractor:
    def __init__(self, gateway: PlaceReader) -> None:
        self._gateway = gateway

    async def __call__(self, id: str, radius: Decimal) -> Optional[List[PlaceDM]]:
        return await self._gateway.read_near_geo_by_id(id, radius)

class GetAllPlacesInteractor:
    def __init__(self, gateway: PlaceReader) -> None:
        self._gateway = gateway

    async def __call__(self, offset:int, limit:int) -> Optional[List[PlaceDM]]:
        return await self._gateway.read_all()


class NewPlaceInteractor:
    def __init__(
        self, db_session: DBSession, gateway: PlaceSaver, uuid_generator: UUIDGenerator
    ) -> None:
        self._db_session = db_session
        self._gateway = gateway
        self._uuid_generator = uuid_generator

    async def __call__(self, dto: NewPlaceDTO) -> str:
        uuid = str(self._uuid_generator())
        place = PlaceDM(
            id=uuid,
            name=dto.name,
            organization_id=dto.organization_id,
            latitude=dto.latitude,
            longitude=dto.longitude,
            description=dto.description,
            logo=dto.logo
        )
        await self._gateway.save(place)
        await self._db_session.commit()
        return uuid


class UpdatePlaceInteractor:
    def __init__(self, db_session: DBSession, gateway: PlaceUpdater) -> None:
        self._db_session = db_session
        self._gateway = gateway

    async def __call__(self,id: str, dto: UpdatePlaceDTO) -> None:
        place = PlaceDM(
            organization_id=dto.organization_id,
            latitude=dto.latitude,
            longitude=dto.longitude,
            description=dto.description,
            logo=dto.logo
        )
        await self._gateway.update(id, place)
        await self._db_session.commit()


class UpdatePlaceGeoInteractor:
    def __init__(
        self, db_session: DBSession, gateway: PlaceGeoUpdater) -> None:
        self._db_session = db_session
        self._gateway = gateway

    async def __call__(self, id: str, dto: UpdateGeoPlaceDTO) -> None:
        place = PlaceDM(
            longitude = dto.longitude,
            latitude = dto.latitude
        )
        await self._gateway.update_geo(id, place)
        await self._db_session.commit()

class UpdatePlaceNameInteractor:
    def __init__(self, db_session: DBSession, gateway: PlaceNameUpdater) -> None:
        self._db_session = db_session
        self._gateway = gateway

    async def __call__(self, id: str, dto: UpdateNamePlaceDTO) -> None:
        place = PlaceDM(name = dto.name)
        await self._gateway.update_name(id, place)
        await self._db_session.commit()

class UpdatePlaceDescriptionInteractor:
    def __init__(self, db_session: DBSession, gateway: PlaceDescriptionUpdater) -> None:
        self._db_session = db_session
        self._gateway = gateway

    async def __call__(self, id: str, dto: UpdateDescriptionPlaceDTO) -> None:
        place = PlaceDM(
            description=dto.description
        )
        await self._gateway.update_description(id, place)
        await self._db_session.commit()

class UpdatePlaceLogoInteractor:
    def __init__(self, db_session: DBSession, gateway: PlaceLogoUpdater) -> None:
        self._db_session = db_session
        self._gateway = gateway

    async def __call__(self, id: str, dto: UpdateLogoPlaceDTO) -> None:
        place = PlaceDM(logo=dto.logo)
        await self._gateway.update_logo(id, place)
        await self._db_session.commit()

class DeletePlaceInteractor:
    def __init__(self, db_session: DBSession, gateway: PlaceDeleter) -> None:
        self._db_session = db_session
        self._gateway = gateway

    async def __call__(self, id: str) -> None:
        await self._gateway.delete(id)
        await self._db_session.commit()