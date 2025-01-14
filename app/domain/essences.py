from decimal import Decimal
from datetime import datetime, time
from typing import List, Optional

from pydantic import BaseModel

from .places import PlaceDM, BaseDM, BaseIdDM

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserDM(BaseIdDM):
    username: str
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
    password: str
    country_id: int
    country: str
    organization: Optional[str] = None
    bio: Optional[str] = None
    phone_number: str
    created_at: datetime
    is_superuser: bool = False
    favorite_cuisines: Optional[List['CuisineDM']] = None
    favorite_music_styles: Optional[List['MusicStyleDM']] = None
    favorite_places: Optional[List['PlaceDM']] = None
    groups: Optional[List['GroupDM']] = None
    messages: Optional[List['MessageDM']] = None
    histories: Optional[List['VideoDM']] = None
    images: Optional[List['ImageDM']] = None

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


