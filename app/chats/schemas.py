from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class UserInDBBase(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class User(UserInDBBase):
    groups: List["Group"] = []
    messages: List["Message"] = []
    histories: List["History"] = []
    images: List["Image"] = []

class ChatBase(BaseModel):
    chat_name: str
    chat_logo: Optional[str] = None
    is_group: bool

class ChatCreate(ChatBase):
    pass

class ChatUpdate(ChatBase):
    pass

class ChatInDBBase(ChatBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Chat(ChatInDBBase):
    users: List[User] = []
    messages: List["Message"] = []
    histories: List["History"] = []
    images: List["Image"] = []

class GroupBase(BaseModel):
    group_name: str

class GroupCreate(GroupBase):
    pass

class GroupUpdate(GroupBase):
    pass

class GroupInDBBase(GroupBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Group(GroupInDBBase):
    members: List[User] = []

class MessageBase(BaseModel):
    content: str
    readed: bool = False

class MessageCreate(MessageBase):
    pass

class MessageUpdate(MessageBase):
    pass

class MessageInDBBase(MessageBase):
    id: int
    user_id: int
    chat_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Message(MessageInDBBase):
    author: User
    chat: Chat

class HistoryBase(BaseModel):
    content: str
    readed: bool = False

class HistoryCreate(HistoryBase):
    pass

class HistoryUpdate(HistoryBase):
    pass

class HistoryInDBBase(HistoryBase):
    id: int
    user_id: int
    chat_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class History(HistoryInDBBase):
    author: User
    chat: Chat

class ImageBase(BaseModel):
    content: str
    readed: bool = False

class ImageCreate(ImageBase):
    pass

class ImageUpdate(ImageBase):
    pass

class ImageInDBBase(ImageBase):
    id: int
    user_id: int
    chat_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Image(ImageInDBBase):
    author: User
    chat: Chat