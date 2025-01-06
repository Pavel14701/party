from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db
from typing import List
from app.schemas.places import PlaceCreate, PlaceRead
from app.db.models.places import Place

router = APIRouter()

@router.post("/places/", response_model=PlaceRead)
async def create_place(place: PlaceCreate, db: AsyncSession = Depends(get_db)):
    db_place = Place(**place.model_dump())
    db.add(db_place)
    await db.commit()
    await db.refresh(db_place)
    return db_place

@router.get("/places/", response_model=List[PlaceRead])
async def read_places(db: AsyncSession = Depends(get_db)):
    result = await db.execute("SELECT * FROM places")
    places = result.fetchall()
    return places
