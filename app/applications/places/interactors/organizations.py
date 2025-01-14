from typing import Optional

from app.applications import UUIDGenerator, DBSession
from app.applications.places.interfaces import (
    OrganizationReader, OrganizationSaver,
    OrganizationUpdater, OrganizationDeleter
)
from app.applications.places.dto import NewOrganizationDTO, UpdateOrganizationDTO 
from app.domain.essences import OrganizationDM


class GetOrganizationInteractor:
    def __init__(
            self,
            gateway: OrganizationReader,
    ) -> None:
        self._gateway = gateway

    async def __call__(self, uuid: str) -> Optional[OrganizationDM]:
        return await self._gateway.read_by_uuid(uuid)

class NewOrganizationInteractor:
    def __init__(
            self,
            db_session: DBSession,
            gateway: OrganizationSaver,
            uuid_generator: UUIDGenerator,
    ) -> None:
        self._db_session = db_session
        self._gateway = gateway
        self._uuid_generator = uuid_generator

    async def __call__(self, dto: NewOrganizationDTO) -> str:
        uuid = str(self._uuid_generator())
        organization = OrganizationDM(
            uuid=uuid,
            name=dto.name,
            unp=dto.unp,
            adress=dto.address,
            latitude=dto.latitude,
            longitude=dto.longitude,
        )
        await self._gateway.save(organization)
        await self._db_session.commit()
        return uuid


class UpdateOrganizationInteractor:
    def __init__(
            self,
            db_session: DBSession,
            gateway: OrganizationUpdater,
    ) -> None:
        self._db_session = db_session
        self._gateway = gateway

    async def __call__(self, dto: UpdateOrganizationDTO) -> None:
        organization = OrganizationDM(
            uuid=dto.uuid,
            name=dto.name,
            unp=dto.unp,
            adress=dto.address,
            latitude=dto.latitude,
            longitude=dto.longitude,
        )
        await self._gateway.update(organization)
        await self._db_session.commit()


class DeleteOrganizationInteractor:
    def __init__(
            self,
            db_session: DBSession,
            gateway: OrganizationDeleter,
    ) -> None:
        self._db_session = db_session
        self._gateway = gateway

    async def __call__(self, uuid: str) -> None:
        await self._gateway.delete(uuid)
        await self._db_session.commit()