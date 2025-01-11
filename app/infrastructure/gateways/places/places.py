from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from decimal import Decimal

from app.infrastructure.models.places  import Place
from app.applications.places.interfaces import (
    PlaceReader, PlaceSaver,
    PlaceUpdater, PlaceDeleter,
)
from app.domain.essences import PlaceDM


class PlaceGateway(
    PlaceDeleter, PlaceReader,
    PlaceSaver, PlaceUpdater
):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def read_by_id(self, id: str) -> Optional[PlaceDM]:
        query = text("""
            SELECT id, name, organization_id, latitude, longitude, description, logo
            FROM place_places
            WHERE id = :id
        """)
        result = await self._session.execute(
            statement=query,
            params={"id": id},
        )
        row:Place
        if row := result.fetchone():
            return PlaceDM(
                id = row.id,
                name = row.name,
                organization_id = row.organization_id,
                latitude = row.latitude,
                longitude = row.longitude,
                description = row.description,
                logo = row.logo
            )
        else:
            return None

    async def read_by_name(self, name:str) -> Optional[List[PlaceDM]]:
        query = text("""
        SELECT id, name, organization_id, latitude, longitude, description, logo
        FROM place_places
        WHERE name = :name
        """)
        result = await self._session.execute(
            statement=query,
            params={"name": name}
        )
        rows:List[Place]
        if rows := result.fetchall():
            return [
                PlaceDM(
                    id=row.id,
                    name=row.name,
                    organization_id=row.organization_id,
                    latitude=row.latitude,
                    longitude=row.longitude,
                    description=row.description,
                    logo=row.logo,
                )
                for row in rows
            ]
        else:
            return None

    async def read_near_geo_by_id(self, id: str, radius: Decimal) -> Optional[List[PlaceDM]]:
        query = text("""
            WITH place_location AS (
                SELECT geom
                FROM place_places
                WHERE id = :id 
            ) 
            SELECT id, name, organization_id, latitude, longitude, description, logo, 
                ST_Distance(geom, pl.geom) AS distance
            FROM place_places, place_location pl 
            WHERE ST_DWithin(geom, pl.geom, :radius) 
            ORDER BY distance
        """)
        result = await self._session.execute(
            statement=query,
            params={
                "id": id,
                "radius": radius
            }
        )
        rows:List[Place]
        if rows := result.fetchall():
            return [
                PlaceDM(
                    id=row.id,
                    name=row.name,
                    organization_id=row.organization_id,
                    latitude=row.latitude,
                    longitude=row.longitude,
                    description=row.description,
                    logo=row.logo,
                )
                for row in rows
            ]
        else:
            return None

    async def read_all(self, offset:int, limit:int) -> Optional[List[PlaceDM]]:
        query = text("""
        SELECT id, name, organization_id, latitude, longitude, description, logo
        FROM place_places
        OFFSET :offset
        LIMIT :limit
        """)
        result = await self._session.execute(
            statement=query,
            params = {
                "offset": offset,
                "limit": limit
            }
        )
        rows:List[Place]
        if rows := result.fetchall():
            return [
                PlaceDM(
                    id=row.id,
                    name=row.name,
                    organization_id=row.organization_id,
                    latitude=row.latitude,
                    longitude=row.longitude,
                    description=row.description,
                    logo=row.logo,
                )
                for row in rows
            ]
        else:
            return None


    async def read_near_geo(self, latitude: Decimal, longitude: Decimal, radius: Decimal) -> Optional[List[PlaceDM]]:
        query = text("""
            SELECT id, name, organization_id, latitude, longitude, description, logo, 
            ST_Distance(geom, ST_SetSRID(ST_MakePoint(:longitude, :latitude), 4326))
            AS distance FROM places 
            WHERE ST_DWithin(geom, ST_SetSRID(ST_MakePoint(:longitude, :latitude), 4326), :radius)
            ORDER BY distance 
        """)
        result = await self._session.execute(
            statement=query,
            params={
                "longitude": longitude,
                "latitude": latitude,
                "radius": radius,
            },
        )
        rows:List[Place]
        if rows := result.fetchall():
            return [
                PlaceDM(
                    id=row.id,
                    name=row.name,
                    organization_id=row.organization_id,
                    latitude=row.latitude,
                    longitude=row.longitude,
                    description=row.description,
                    logo=row.logo,
                )
                for row in rows
            ]
        else:
            return None

    async def read_near_geo_by_id(self, id:str, radius:Decimal) -> Optional[List[Place]]: 
        pass

    async def save(self, place: PlaceDM) -> None:
        query = text("""
            INSERT INTO place_places
            (id, name, organization_id, latitude,
            longitude, geom, description, logo)
            VALUES 
            (:id, :name, :organization_id, :latitude, :longtitude,
            geom = ST_SetSRID(ST_MakePoint(:longitude, :latitude), 4326),
            :description, :logo)
        """)
        await self._session.execute(
            statement=query,
            params={
                "id": place.id,
                "name": place.name,
                "organization_id": place.organization_id,
                "latitude": place.latitude,
                "logitude": place.longitude,
                "description": place.description,
                "logo": place.logo
            },
        )

    async def update(self, id: str, place: PlaceDM) -> None:
        query = text("""
            UPDATE place_places 
            SET name = :new_name, organization_id = :new_organization_id,
                latitude = :new_latitude, longitude = :new_longitude,
                description = :new_description, logo = :new_logo 
            WHERE id = :id
        """)
        await self._session.execute(
            statement = query,
            params = {
                "id": id,
                "new_name": place.name,
                "new_organization_id": place.organization_id,
                "new_latitude": place.latitude,
                "new_longitude": place.longitude,
                "new_description": place.description,
                "new_logo": place.logo
            },
        )

    async def update_geo(self, id: str, place: PlaceDM) -> None:
        query = text("""
            UPDATE place_places 
            SET latitude = :new_latitude, longitude = :new_longitude 
            WHERE id = :id
        """)
        await self._session.execute(
            statement=query,
            params={
                "id": id,
                "new_latitude": place.latitude,
                "new_longitude": place.longitude
            },
        )

    async def update_name(self, id: str, place: PlaceDM) -> None:
        query = text("""
            UPDATE place_places 
            SET name = :new_name
            WHERE id = :id
        """)
        await self._session.execute(
            statement=query,
            params={
                "id": id,
                "new_name": place.name,
            },
        )

    async def update_description(self, id: str, place: PlaceDM) -> None:
        query = text("""
            UPDATE place_places
            SET description = :new_description
            WHERE id = :id
        """)
        await self._session.execute(
            statement=query,
            params={
                "id": id,
                "new_description": place.description,
            },
        )

    async def update_logo(self, id: str, place: PlaceDM) -> None:
        query = text("""
            UPDATE place_places 
            SET logo = :new_logo
            WHERE id = :id
        """)
        await self._session.execute(
            statement=query,
            params={
                "id": id,
                "new_logo": place.logo,
            },
        )

    async def delete(self, id: str) -> None:
        query = text("""
            DELETE FROM place_places
            WHERE id = :id
        """)
        await self._session.execute(
            statement=query,
            params={
                "id":id
            },
        )