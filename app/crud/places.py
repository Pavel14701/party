from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import places as models
from app.schemas import places as schemas

async def create_place(db: AsyncSession, place: schemas.PlaceCreate):
    db_place = models.Place(
        name=place.name,
        description=place.description,
        logo=place.logo,
        video=place.video,
        categories=[models.Category(name=cat.name) for cat in place.categories],
        labels=[models.Label(name=label.name) for label in place.labels],
        services=[models.Service(name=service.name, price=service.price) for service in place.services],
        images=[models.Image(url=img.url) for img in place.images],
        menu_items=[models.MenuItem(name=item.name, price=item.price, category=models.Category(name=item.category.name)) for item in place.menu_items]
    )
    db.add(db_place)
    await db.commit()
    return db_place

async def get_places(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Place).offset(skip).limit(limit))
    return result.scalars().all()
