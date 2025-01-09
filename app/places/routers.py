from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.session import get_session
from typing import List
from app.places.schemas import PlaceRead
from app.places import crud as crud

router = APIRouter()

@router.post("/places/", response_model=PlaceRead)
async def create_place(db: AsyncSession = Depends(get_session)):
    db_place = await crud.create_place(db, db_place)
    return db_place

@router.get("/places/", response_model=List[PlaceRead])
async def read_places(
    skip:int=Query(0, ge=0),
    limit:int=Query(10, ge=1),
    db:AsyncSession=Depends(get_session)
):
    return await crud.get_places(db, skip, limit)
