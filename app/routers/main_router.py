from fastapi import APIRouter, Depends
from app.dependencies import container
from app.services.my_service import MyService

router = APIRouter()

def get_my_service() -> MyService:
    return container.get(MyService)

@router.get("/service")
async def service_route(my_service: MyService = Depends(get_my_service)):
    result = my_service.do_something()
    return {"message": result}
