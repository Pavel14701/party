from typing import Annotated
from uuid import UUID
from http import HTTPStatus

from dishka.integrations.base import FromDishka as Depends
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.applications.places.interactors import (
    GetPlaceInteractor, NewPlaceInteractor,
    UpdatePlaceInteractor, DeletePlaceInteractor
) 
from app.controllers.schemas import PlaceSchema



class HttpPlaceController:
    router = APIRouter(prefix='/place')

    @router.get("/{place_id}", response_model=PlaceSchema)
    @inject
    async def get_place(
        self, 
        place_id: Annotated[UUID, str], 
        interactor: Depends[GetPlaceInteractor]
    ) -> PlaceSchema:
        place_dm = await interactor(uuid=str(place_id))
        if not place_dm:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Place not found")
        return PlaceSchema(
            uuid=place_dm.uuid,
            name=place_dm.name,
            organization_id=place_dm.organization_id,
            latitude=place_dm.latitude,
            longitude=place_dm.longitude,
            description=place_dm.description,
            logo=place_dm.logo
        )

    @router.update("/{place_id}", response_model=PlaceSchema)
    @inject
    async def update_place(
        self,
        place_id: Annotated[UUID, str],
        interactor: Depends[UpdatePlaceInteractor]
    ) -> PlaceSchema:
        place_dm = await interactor()




