from pydantic import BaseModel
from typing import List, Optional
from datetime import time
from enum import Enum

class DayOfWeek(str, Enum):
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
    Saturday = "Saturday"
    Sunday = "Sunday"

class OrganizationBase(BaseModel):
    name: str
    unp: str
    address: str
    current_account: str
    latitude: float
    longitude: float

class OrganizationCreate(OrganizationBase):
    pass

class Organization(OrganizationBase):
    id: int
    places: List["Place"] = []

    class Config:
        orm_mode: True

class PlaceBase(BaseModel):
    name: str
    latitude: float
    longitude: float
    description: Optional[str]
    logo: Optional[str]

class PlaceCreate(PlaceBase):
    organization_id: int

class Place(PlaceBase):
    id: int
    organization: Organization
    videos: List["Video"] = []
    images: List["Image"] = []
    services: List["Service"] = []
    menu_items: List["MenuItem"] = []
    categories: List["Category"] = []
    labels: List["Label"] = []
    reviews_google: List["GoogleReviews"] = []
    reviews_yandex: List["YandexReviews"] = []

    class Config:
        orm_mode: True

class GoogleReviewsBase(BaseModel):
    reviewer_name: str
    review: str
    review_mark: float

class GoogleReviewsCreate(GoogleReviewsBase):
    place_id: int

class GoogleReviews(GoogleReviewsBase):
    id: int
    place: Place

    class Config:
        orm_mode: True

class YandexReviewsBase(BaseModel):
    reviewer_name: str
    review: str
    review_mark: float

class YandexReviewsCreate(YandexReviewsBase):
    place_id: int

class YandexReviews(YandexReviewsBase):
    id: int
    place: Place

    class Config:
        orm_mode: True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    places: List[Place] = []

    class Config:
        orm_mode: True

class LabelBase(BaseModel):
    name: str

class LabelCreate(LabelBase):
    pass

class Label(LabelBase):
    id: int
    places: List[Place] = []

    class Config:
        orm_mode: True

class ImageBase(BaseModel):
    alt: Optional[str]
    url: str

class ImageCreate(ImageBase):
    place_id: int

class Image(ImageBase):
    id: int
    place: Place

    class Config:
        orm_mode: True

class VideoBase(BaseModel):
    url: str

class VideoCreate(VideoBase):
    place_id: int

class Video(VideoBase):
    id: int
    place: Place

    class Config:
        orm_mode: True

class ServiceBase(BaseModel):
    name: str
    price: float

class ServiceCreate(ServiceBase):
    place_id: int

class Service(ServiceBase):
    id: int
    place: Place

    class Config:
        orm_mode: True

class MenuItemBase(BaseModel):
    name: str
    price: float

class MenuItemCreate(MenuItemBase):
    category_id: int
    place_id: int

class MenuItem(MenuItemBase):
    id: int
    place: Place
    category: "MenuCategory"

    class Config:
        orm_mode: True

class MenuCategoryBase(BaseModel):
    name: str

class MenuCategoryCreate(MenuCategoryBase):
    pass

class MenuCategory(MenuCategoryBase):
    id: int
    menu_items: List[MenuItem] = []

    class Config:
        orm_mode: True

class PlaceHoursBase(BaseModel):
    day_of_week: DayOfWeek
    open_time: time
    close_time: time

class PlaceHoursCreate(PlaceHoursBase):
    business_id: int

class PlaceHours(PlaceHoursBase):
    id: int
    business: Place

    class Config:
        orm_mode: True
