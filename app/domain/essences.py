from decimal import Decimal
from datetime import datetime, time
from typing import List, Optional
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

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

class UserDM(BaseIdDM):
    username: str
    firstname: str
    lastname: str
    email: Optional[str]
    password: str
    country_id: int
    bio: Optional[str]
    phone_number: str
    created_at: datetime
    favorite_cuisines: List['CuisineDM']
    favorite_music_styles: List['MusicStyleDM']
    favorite_places: List['PlaceDM']
    groups: List['GroupDM']
    messages: List['MessageDM']
    histories: List['VideoDM']
    images: List['ImageDM']

class ChatDM(BaseIdDM):
    chat_name: str
    chat_logo: Optional[str]
    is_group: bool
    created_at: datetime
    messages: List['MessageDM']
    users: List['UserDM']
    histories: List['VideoDM']
    images: List['ImageDM']

class GroupDM(BaseIdDM):
    group_name: str
    created_at: datetime
    members: List['UserDM']

class BaseChatMessageDM(BaseIdDM):
    user_id: str
    chat_id: str
    readed: bool
    created_at: datetime
    updated_at: datetime
    author: 'UserDM'
    chat: 'ChatDM'

class MessageDM(BaseChatMessageDM):
    content: str

class VideoDM(BaseChatMessageDM):
    content: str
    description: Optional[str]

class ImageDM(BaseChatMessageDM):
    content: str
    description: Optional[str]

class CountryDM(BaseIdDM):
    name: str
    code: str

class CuisineDM(BaseDM):
    pass

class MusicStyleDM(BaseDM):
    pass

class OrganizationDM(BaseDM):
    unp: str
    address: str
    current_account: str  # Рассчётный счёт
    latitude: Decimal  # Широта
    longitude: Decimal  # Долгота

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