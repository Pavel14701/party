from dishka.integrations.base import FromDishka as Depends
from faststream.rabbit import RabbitRouter

from app.applications.places.dto import NewPlaceDTO
from app.applications.places.interactors import NewPlaceInteractor
from app.controllers.schemas import PlaceSchema

AMQPController = RabbitRouter()


@AMQPController.subscriber("create_place")
@AMQPController.publisher("place_statuses")
async def handle(data: PlaceSchema, interactor: Depends[NewPlaceInteractor]) -> str:
    dto = NewPlaceDTO(
        title=data.title,
        pages=data.pages,
        is_read=data.is_read
    )
    return await interactor(dto)