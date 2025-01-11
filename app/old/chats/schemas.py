from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MessageRead(BaseModel):
    id: int
    content: str
    user_id: int
    chat_id: int
    readed: bool
    created_at: datetime

    class Config:
        orm_mode = True

class HistoryRead(BaseModel):
    id: int
    content: str
    readed: bool
    user_id: int
    chat_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class ImageRead(BaseModel):
    id: int
    content: str
    user_id: int
    chat_id: int
    readed: bool
    created_at: datetime

    class Config:
        orm_mode = True

class ChatBase(BaseModel):
    chat_name: str
    chat_logo: Optional[str] = None
    is_group: bool

class ChatCreate(ChatBase):
    pass

class ChatRead(BaseModel):
    id: int
    chat_name: str
    chat_logo: Optional[str]
    is_group: bool
    created_at: datetime
    messages: List[MessageRead] = []
    users: List[int] = []
    histories: List[HistoryRead] = []
    images: List[ImageRead] = []

    class Config:
        orm_mode = True

class GroupBase(BaseModel):
    group_name: str

class GroupCreate(GroupBase):
    pass

class GroupRead(BaseModel):
    id: int
    group_name: str
    created_at: datetime
    members: List[int] = []

    class Config:
        orm_mode = True

class MessageBase(BaseModel):
    content: str
    user_id: int
    chat_id: int
    readed: bool

class MessageCreate(MessageBase):
    pass

class MessageReadFull(MessageBase):
    id: int
    created_at: datetime
    author: int

    class Config:
        orm_mode = True

class HistoryBase(BaseModel):
    content: str
    readed: bool
    user_id: int
    chat_id: int

class HistoryCreate(HistoryBase):
    pass

class HistoryReadFull(HistoryBase):
    id: int
    created_at: datetime
    author: int

    class Config:
        orm_mode = True

class ImageBase(BaseModel):
    content: str
    user_id: int
    chat_id: int
    readed: bool

class ImageCreate(ImageBase):
    pass

class ImageReadFull(ImageBase):
    id: int
    created_at: datetime
    author: int

    class Config:
        orm_mode = True
