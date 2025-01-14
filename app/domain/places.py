from decimal import Decimal
from datetime import datetime, time
from typing import List, Optional
from pydantic import BaseModel

class BaseIdDM(BaseModel):
    id: Optional[str] = None

    class Config:
        from_attributes=True

class BaseDM(BaseIdDM):
    name: Optional[str] = None

class BaseReview(BaseIdDM):
    reviewer_name: Optional[str]
    review: str
    review_mark: Decimal
    place_id: str

class PlaceDM(BaseDM):
    organization_id: Optional[str] = None
    latitude: Optional[Decimal] = None
    longitude: Optional[Decimal] = None
    description: Optional[str] = None
    logo: Optional[str] = None

class GoogleReviewsDM(BaseReview):
    pass

class YandexReviewsDM(BaseReview):
    pass

class CategoryDM(BaseDM):
    pass

class LabelDM(BaseModel):
    pass

class ImageDM(BaseIdDM):
    alt: str
    url: str
    place_id: str

class VideoDM(BaseIdDM):
    url: str
    place_id: str

class ServiceDM(BaseDM):
    price: Decimal
    place_id: str

class MenuItemDM(BaseDM):
    price: Decimal
    category_id: str
    place_id: str

class MenuCategoryDM(BaseDM):
    pass

class PlaceHoursDM(BaseIdDM):
    day_of_week: str
    open_time: time
    close_time: time
    is_weekend: bool
    place_id: str
    comment: Optional[str] = None

class OrganizationDM(BaseDM):
    unp: str
    address: str
    current_account: str  # Рассчётный счёт
    latitude: Decimal  # Широта
    longitude: Decimal  # Долгота
