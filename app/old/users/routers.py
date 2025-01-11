from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.infrastructure.database import get_session
from app.users.schemas import (
    UserCreate, UserRead, CountryCreate, CountryRead,
    CuisineCreate, CuisineRead, MusicStyleCreate, MusicStyleRead,
    PlaceCreate, PlaceRead
)
from app.users.crud import (
    create_user, get_user, get_users, update_user, delete_user,
    create_country, get_country, get_countries, update_country, delete_country,
    create_cuisine, get_cuisine, get_cuisines, update_cuisine, delete_cuisine,
    create_music_style, get_music_style, get_music_styles, update_music_style, delete_music_style,
    create_place, get_place, get_places, update_place, delete_place
)

router = APIRouter()

# Маршруты для User
@router.post("/users/", response_model=UserRead)
async def create_user_endpoint(
    user: UserCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_user(db, user)

@router.get("/users/{user_id}", response_model=UserRead)
async def read_user(
    user_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_user = await get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users/", response_model=List[UserRead])
async def read_users(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_users(db, skip, limit)

@router.put("/users/{user_id}", response_model=UserRead)
async def update_user_endpoint(
    user_id: int, user: UserCreate,
    db: AsyncSession = Depends(get_session)
):
    db_user = await update_user(db, user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/users/{user_id}", response_model=UserRead)
async def delete_user_endpoint(
    user_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_user = await delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Маршруты для Country
@router.post("/countries/", response_model=CountryRead)
async def create_country_endpoint(
    country: CountryCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_country(db, country)

@router.get("/countries/{country_id}", response_model=CountryRead)
async def read_country(
    country_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_country = await get_country(db, country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country

@router.get("/countries/", response_model=List[CountryRead])
async def read_countries(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_countries(db, skip, limit)

@router.put("/countries/{country_id}", response_model=CountryRead)
async def update_country_endpoint(
    country_id: int, country: CountryCreate,
    db: AsyncSession = Depends(get_session)
):
    db_country = await update_country(db, country_id, country)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country

@router.delete("/countries/{country_id}", response_model=CountryRead)
async def delete_country_endpoint(
    country_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_country = await delete_country(db, country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country

# Маршруты для Cuisine
@router.post("/cuisines/", response_model=CuisineRead)
async def create_cuisine_endpoint(
    cuisine: CuisineCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_cuisine(db, cuisine)

@router.get("/cuisines/{cuisine_id}", response_model=CuisineRead)
async def read_cuisine(
    cuisine_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_cuisine = await get_cuisine(db, cuisine_id)
    if db_cuisine is None:
        raise HTTPException(status_code=404, detail="Cuisine not found")
    return db_cuisine

@router.get("/cuisines/", response_model=List[CuisineRead])
async def read_cuisines(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_cuisines(db, skip, limit)

@router.put("/cuisines/{cuisine_id}", response_model=CuisineRead)
async def update_cuisine_endpoint(
    cuisine_id: int, cuisine: CuisineCreate,
    db: AsyncSession = Depends(get_session)
):
    db_cuisine = await update_cuisine(db, cuisine_id, cuisine)
    if db_cuisine is None:
        raise HTTPException(status_code=404, detail="Cuisine not found")
    return db_cuisine

@router.delete("/cuisines/{cuisine_id}", response_model=CuisineRead)
async def delete_cuisine_endpoint(
    cuisine_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_cuisine = await delete_cuisine(db, cuisine_id)
    if db_cuisine is None:
        raise HTTPException(status_code=404, detail="Cuisine not found")
    return db_cuisine

# Маршруты для MusicStyle
@router.post("/music_styles/", response_model=MusicStyleRead)
async def create_music_style_endpoint(
    music_style: MusicStyleCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_music_style(db, music_style)

@router.get("/music_styles/{music_style_id}", response_model=MusicStyleRead)
async def read_music_style(
    music_style_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_music_style = await get_music_style(db, music_style_id)
    if db_music_style is None:
        raise HTTPException(status_code=404, detail="Music style not found")
    return db_music_style

@router.get("/music_styles/", response_model=List[MusicStyleRead])
async def read_music_styles(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_music_styles(db, skip, limit)

@router.put("/music_styles/{music_style_id}", response_model=MusicStyleRead)
async def update_music_style_endpoint(
    music_style_id: int, music_style: MusicStyleCreate,
    db: AsyncSession = Depends(get_session)
):
    db_music_style = await update_music_style(db, music_style_id, music_style)
    if db_music_style is None:
        raise HTTPException(status_code=404, detail="Music style not found")
    return db_music_style

@router.delete("/music_styles/{music_style_id}", response_model=MusicStyleRead)
async def delete_music_style_endpoint(
    music_style_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_music_style = await delete_music_style(db, music_style_id)
    if db_music_style is None:
        raise HTTPException(status_code=404, detail="Music style not found")
    return db_music_style

# Маршруты для Place
@router.post("/places/", response_model=PlaceRead)
async def create_place_endpoint(
    place: PlaceCreate,
    db: AsyncSession = Depends(get_session)
):
    return await create_place(db, place)

@router.get("/places/{place_id}", response_model=PlaceRead)
async def read_place(
    place_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_place = await get_place(db, place_id)
    if db_place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_place

@router.get("/places/", response_model=List[PlaceRead])
async def read_places(
    skip: int = 0, limit: int = 10,
    db: AsyncSession = Depends(get_session)
):
    return await get_places(db, skip, limit)

@router.put("/places/{place_id}", response_model=PlaceRead)
async def update_place_endpoint(
    place_id: int, place: PlaceCreate,
    db: AsyncSession = Depends(get_session)
):
    db_place = await update_place(db, place_id, place)
    if db_place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_place

@router.delete("/places/{place_id}", response_model=PlaceRead)
async def delete_place_endpoint(
    place_id: int,
    db: AsyncSession = Depends(get_session)
):
    db_place = await delete_place(db, place_id)
    if db_place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_place
