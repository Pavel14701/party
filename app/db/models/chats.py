from sqlalchemy import (
    Column, BigInteger,
    String, ForeignKey, TIMESTAMP,
    Boolean, Table
)
from sqlalchemy.sql import func
from sqlalchemy.orm import (relationship, DeclarativeMeta)
from app.db.base_class import _Base

Base: DeclarativeMeta = _Base()

class User(Base):
    __tablename__ = "chat_users"
    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(length=255), unique=True, nullable=False)
    email = Column(String(length=255), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    groups = relationship("Group", secondary="chat_user_groups", back_populates="members")
    messages = relationship("Message", back_populates="author")
    histories = relationship("History", back_populates="author")
    images = relationship("Image", back_populates="author")

class Chat(Base):
    __tablename__ = "chat_chats"
    id = Column(BigInteger, primary_key=True, index=True)
    chat_name = Column(String(length=255), nullable=False)
    chat_logo = Column(String(length=255), nullable=True)
    is_group = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    messages = relationship("Message", back_populates="chat")
    users = relationship("User", secondary="chat_chat_users", back_populates="chats")
    histories = relationship("History", back_populates="chat")
    images = relationship("Image", back_populates="chat")

class Group(Base):
    __tablename__ = "chat_groups"
    id = Column(BigInteger, primary_key=True, index=True)
    group_name = Column(String(length=255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    members = relationship("User", secondary="chat_user_groups", back_populates="groups")

class Message(Base):
    __tablename__ = "chat_messages"
    id = Column(BigInteger, primary_key=True, index=True)
    content = Column(String(length=4096), nullable=False)
    user_id = Column(BigInteger, ForeignKey("chat_users.id"), nullable=False)
    chat_id = Column(BigInteger, ForeignKey("chat_chats.id"), nullable=False)
    readed = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    author = relationship("User", back_populates="messages")
    chat = relationship("Chat", back_populates="messages")

class History(Base):
    __tablename__ = "chat_histories"
    id = Column(BigInteger, primary_key=True, index=True)
    content = Column(String(length=255), nullable=False)
    readed = Column(Boolean, default=False)
    user_id = Column(BigInteger, ForeignKey("chat_users.id"), nullable=False)
    chat_id = Column(BigInteger, ForeignKey("chat_chats.id"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    author = relationship("User", back_populates="histories")
    chat = relationship("Chat", back_populates="histories")

class Image(Base):
    __tablename__ = "chat_images"
    id = Column(BigInteger, primary_key=True, index=True)
    content = Column(String(length=255), nullable=False)
    user_id = Column(BigInteger, ForeignKey("chat_users.id"), nullable=False)
    chat_id = Column(BigInteger, ForeignKey("chat_chats.id"), nullable=False)
    readed = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    author = relationship("User", back_populates="images")
    chat = relationship("Chat", back_populates="images")

chat_users = Table(
    'chat_chat_users', Base.metadata,
    Column('chat_id', BigInteger, ForeignKey('chat_chats.id', ondelete='CASCADE'), primary_key=True),
    Column('user_id', BigInteger, ForeignKey('chat_users.id', ondelete='CASCADE'), primary_key=True)
)

user_groups = Table(
    'chat_user_groups', Base.metadata,
    Column('user_id', BigInteger, ForeignKey('chat_users.id', ondelete='CASCADE'), primary_key=True),
    Column('group_id', BigInteger, ForeignKey('chat_groups.id', ondelete='CASCADE'), primary_key=True)
)
