from typing import AsyncIterable
from uuid import uuid4

from dishka import Provider, Scope, provide, AnyOf, from_context
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.applications import interfaces
from app.applications.places.interfaces import *
from app.applications.places.interactors import *
from app.core.config import Config
from app.infrastructure.database import new_session_maker
from app.infrastructure.gateways.places import PlaceGateway


class AppProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_uuid_generator(self) -> interfaces.UUIDGenerator:
        return uuid4

    @provide(scope=Scope.APP)
    def get_session_maker(self, config: Config) -> async_sessionmaker[AsyncSession]:
        return new_session_maker(config.postgres)

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self, session_maker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AnyOf[AsyncSession, interfaces.DBSession,]]:
        async with session_maker() as session:
            yield session

    place_gateway = provide(
        PlaceGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[
            PlaceDeleter, PlaceReader, PlaceUpdater, PlaceSaver,
            PlaceGeoUpdater, PlaceLogoUpdater, PlaceDescriptionUpdater,
            PlaceNameUpdater
        ]
    )

    get_place_by_id_interactor = provide(GetPlaceByIdInteractor, scope=Scope.REQUEST)
    get_place_by_name_interactor = provide(GetPlaceByNameInteractor, scope=Scope.REQUEST)
    get_places_by_user_geo_interactor = provide(GetPlaceByGeoInteractor, scope=Scope.REQUEST)
    get_places_by_id_place_interactor = provide(GetPlaceByIdGeoInteractor, scope=Scope.REQUEST)
    get_all_places_interactor = provide(GetAllPlacesInteractor, scope=Scope.REQUEST)
    create_new_place_interactor = provide(NewPlaceInteractor, scope=Scope.REQUEST)
    update_place_interactor = provide(UpdatePlaceInteractor, scope=Scope.REQUEST)
    update_place_geo_interactor = provide(UpdatePlaceGeoInteractor, scope=Scope.REQUEST)
    update_place_name_interactor = provide(UpdatePlaceNameInteractor, scope=Scope.REQUEST)
    update_place_description_interactor = provide(UpdatePlaceDescriptionInteractor, scope=Scope.REQUEST)
    update_place_logo_interactor = provide(UpdatePlaceLogoInteractor, scope=Scope.REQUEST)
    delete_place_logo_interactor = provide(DeletePlaceInteractor, scope=Scope.REQUEST)
    