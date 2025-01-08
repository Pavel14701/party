from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.places import models as models
from app.places import schemas as schemas

async def create_place(db: AsyncSession, place: schemas.PlaceCreate):
    place_data = place.model_dump() 
    db_place = models.Place(**place_data)
    db.add(db_place)
    await db.commit()
    await db.refresh(db_place)
    return db_place

async def get_places(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Place).offset(skip).limit(limit))
    return result.scalars().all()
