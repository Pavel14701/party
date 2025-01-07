from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from typing import List
from app.schemas.places import PlaceCreate, PlaceRead
from app.db.models.places import Place
from sqlalchemy.future import select

router = APIRouter()

@router.post("/places/", response_model=PlaceRead)
async def create_place(place: PlaceCreate, db: AsyncSession = Depends(get_session)):
    db_place = Place(**place.model_dump())
    db.add(db_place)
    await db.commit()
    await db.refresh(db_place)
    return db_place

@router.get("/places/", response_model=List[PlaceRead]) 
async def read_places(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Place)) 
    return result.scalars().all() 
