from pydantic import BaseModel, field_validator, model_validator
from typing import List, Optional

class CuisineRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class MusicStyleRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class PlaceRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class CountryRead(BaseModel):
    id: int
    name: str
    code: str

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    email: Optional[str] = None
    phone_number: Optional[str] = None
    country_id: int

    @model_validator(mode='before')
    def check_email_or_phone(cls, values:dict) -> dict:
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