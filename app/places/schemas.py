from pydantic import BaseModel
from typing import List, Optional

class Service(BaseModel):
    name: str
    price: float

class Image(BaseModel):
    url: str

class Category(BaseModel):
    name: str

class Label(BaseModel):
    name: str

class MenuItem(BaseModel):
    name: str
    price: float
    category: Optional[Category] = None

class PlaceCreate(BaseModel):
    name: str
    description: str
    logo: str
    video: str
    categories: List[Category] = []
    labels: List[Label] = []
    services: List[Service] = []
    images: List[Image] = []
    menu_items: List[MenuItem] = []

class PlaceRead(BaseModel):
    id: int
    name: str
    description: str
    logo: str
    video: str
    categories: List[Category] = []
    labels: List[Label] = []
    services: List[Service] = []
    images: List[Image] = []
    menu_items: List[MenuItem] = []

    class Config:
        orm_mode = True
