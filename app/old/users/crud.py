from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.infrastructure.models.users import User, Country, Cuisine, MusicStyle, Place
from app.users.schemas import (
    UserCreate, UserRead, CountryCreate, CountryRead,
    CuisineCreate, CuisineRead, MusicStyleCreate, MusicStyleRead,
    PlaceCreate, PlaceRead
)

# CRUD operations for User
async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_user(db: AsyncSession, user_id: int):
    return await db.get(User, user_id)

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()

async def update_user(db: AsyncSession, user_id: int, user: UserCreate):
    db_user = await get_user(db, user_id)
    if db_user:
        for key, value in user.dict().items():
            setattr(db_user, key, value)
        await db.commit()
        await db.refresh(db_user)
    return db_user

async def delete_user(db: AsyncSession, user_id: int):
    db_user = await get_user(db, user_id)
    if db_user:
        await db.delete(db_user)
        await db.commit()
    return db_user

# CRUD operations for Country
async def create_country(db: AsyncSession, country: CountryCreate):
    db_country = Country(**country.dict())
    db.add(db_country)
    await db.commit()
    await db.refresh(db_country)
    return db_country

async def get_country(db: AsyncSession, country_id: int):
    return await db.get(Country, country_id)

async def get_countries(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Country).offset(skip).limit(limit))
    return result.scalars().all()

async def update_country(db: AsyncSession, country_id: int, country: CountryCreate):
    db_country = await get_country(db, country_id)
    if db_country:
        for key, value in country.dict().items():
            setattr(db_country, key, value)
        await db.commit()
        await db.refresh(db_country)
    return db_country

async def delete_country(db: AsyncSession, country_id: int):
    db_country = await get_country(db, country_id)
    if db_country:
        await db.delete(db_country)
        await db.commit()
    return db_country

# CRUD operations for Cuisine
async def create_cuisine(db: AsyncSession, cuisine: CuisineCreate):
    db_cuisine = Cuisine(**cuisine.dict())
    db.add(db_cuisine)
    await db.commit()
    await db.refresh(db_cuisine)
    return db_cuisine

async def get_cuisine(db: AsyncSession, cuisine_id: int):
    return await db.get(Cuisine, cuisine_id)

async def get_cuisines(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Cuisine).offset(skip).limit(limit))
    return result.scalars().all()

async def update_cuisine(db: AsyncSession, cuisine_id: int, cuisine: CuisineCreate):
    db_cuisine = await get_cuisine(db, cuisine_id)
    if db_cuisine:
        for key, value in cuisine.dict().items():
            setattr(db_cuisine, key, value)
        await db.commit()
        await db.refresh(db_cuisine)
    return db_cuisine

async def delete_cuisine(db: AsyncSession, cuisine_id: int):
    db_cuisine = await get_cuisine(db, cuisine_id)
    if db_cuisine:
        await db.delete(db_cuisine)
        await db.commit()
    return db_cuisine

# CRUD operations for MusicStyle
async def create_music_style(db: AsyncSession, music_style: MusicStyleCreate):
    db_music_style = MusicStyle(**music_style.dict())
    db.add(db_music_style)
    await db.commit()
    await db.refresh(db_music_style)
    return db_music_style

async def get_music_style(db: AsyncSession, music_style_id: int):
    return await db.get(MusicStyle, music_style_id)

async def get_music_styles(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(MusicStyle).offset(skip).limit(limit))
    return result.scalars().all()

async def update_music_style(db: AsyncSession, music_style_id: int, music_style: MusicStyleCreate):
    db_music_style = await get_music_style(db, music_style_id)
    if db_music_style:
        for key, value in music_style.dict().items():
            setattr(db_music_style, key, value)
        await db.commit()
        await db.refresh(db_music_style)
    return db_music_style

async def delete_music_style(db: AsyncSession, music_style_id: int):
    db_music_style = await get_music_style(db, music_style_id)
    if db_music_style:
        await db.delete(db_music_style)
        await db.commit()
    return db_music_style

# CRUD operations for Place
async def create_place(db: AsyncSession, place: PlaceCreate):
    db_place = Place(**place.dict())
    db.add(db_place)
    await db.commit()
    await db.refresh(db_place)
    return db_place

async def get_place(db: AsyncSession, place_id: int):
    return await db.get(Place, place_id)

async def get_places(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Place).offset(skip).limit(limit))
    return result.scalars().all()

async def update_place(db: AsyncSession, place_id: int, place: PlaceCreate):
    db_place = await get_place(db, place_id)
    if db_place:
        for key, value in place.dict().items():
            setattr(db_place, key, value)
        await db.commit()
        await db.refresh(db_place)
    return db_place

async def delete_place(db: AsyncSession, place_id: int):
    db_place = await get_place(db, place_id)
    if db_place:
        await db.delete(db_place)
        await db.commit()
    return db_place
