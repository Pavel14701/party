from pydantic import BaseModel, EmailStr, field_validator, model_validator
from typing import List, Optional
from datetime import datetime

# Модель для ассоциаций
class AssociationBase(BaseModel):
    user_id: int
    id: int

# Ассоциации для избранных кухонь, стилей музыки и мест
class FavoriteCuisineBase(AssociationBase):
    cuisine_id: int

class FavoriteMusicStyleBase(AssociationBase):
    music_style_id: int

class FavoritePlaceBase(AssociationBase):
    place_id: int

# Модели для данных
class CountryBase(BaseModel):
    name: str
    code: str

class CountryCreate(CountryBase):
    pass

class CountryRead(BaseModel):
    id: int
    name: str
    code: str

    class Config:
        orm_mode = True

class Country(CountryBase):
    id: int

    class Config:
        orm_mode = True

class CuisineBase(BaseModel):
    name: str

class CuisineCreate(CuisineBase):
    pass

class CuisineRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class Cuisine(CuisineBase):
    id: int
    users: List["User"] = []

    class Config:
        orm_mode = True

class MusicStyleBase(BaseModel):
    name: str

class MusicStyleCreate(MusicStyleBase):
    pass

class MusicStyleRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class MusicStyle(MusicStyleBase):
    id: int
    users: List["User"] = []

    class Config:
        orm_mode = True

class PlaceBase(BaseModel):
    name: str

class PlaceCreate(PlaceBase):
    pass

class PlaceRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class Place(PlaceBase):
    id: int
    users: List["User"] = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    country_id: int
    bio: Optional[str]
    phone_number: str

class UserCreate(UserBase):
    @model_validator(mode='before')
    def check_email_or_phone(cls, values: dict) -> dict:
        email = values.get('email')
        phone_number = values.get('phone_number')
        if not email and not phone_number:
            raise ValueError("Either email or phone number must be provided")
        return values

class UserRead(BaseModel):
    id: int
    username: str
    email: Optional[str]
    phone_number: Optional[str]
    country: Optional[CountryRead]
    favorite_cuisines: List[CuisineRead]
    favorite_music_styles: List[MusicStyleRead]
    favorite_places: List[PlaceRead]

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    country: Country
    favorite_cuisines: List[Cuisine] = []
    favorite_music_styles: List[MusicStyle] = []
    favorite_places: List[Place] = []
    created_at: datetime

    class Config:
        orm_mode = True
