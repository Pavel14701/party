from typing import AsyncIterable
from uuid import uuid4

from dishka import Provider, Scope, provide, AnyOf, from_context
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.applications import interfaces
from app.applications.places.interfaces import (
    PlaceReader, PlaceUpdater,
    PlaceSaver, PlaceDeleter
)
from app.applications.places.interactors import (
    GetPlaceInteractor, UpdatePlaceInteractor,
    NewPlaceInteractor, DeletePlaceInteractor
)
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
    async def get_session(self, session_maker: async_sessionmaker[AsyncSession]) -> AsyncIterable[AnyOf[
        AsyncSession,
        interfaces.DBSession,
    ]]:
        async with session_maker() as session:
            yield session

    pace_gateway = provide(
        PlaceGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[interfaces.PlaceReader, interfaces.PlaceSaver]
    )

    get_place_interactor = provide(GetPlaceInteractor, scope=Scope.REQUEST)
    create_new_place_interactor = provide(NewPlaceInteractor, scope=Scope.REQUEST)