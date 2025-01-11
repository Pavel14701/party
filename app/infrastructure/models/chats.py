import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from datetime import datetime

from app.core.base_class import Base

chat_users = sa.Table(
    'chat_chat_users', Base.metadata,
    sa.Column('chat_id', UUID(as_uuid=True), sa.ForeignKey('chat_chats.id', ondelete='CASCADE'), primary_key=True),
    sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('chat_users.id', ondelete='CASCADE'), primary_key=True)
)

user_groups = sa.Table(
    'chat_user_groups', Base.metadata,
    sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('chat_users.id', ondelete='CASCADE'), primary_key=True),
    sa.Column('group_id', UUID(as_uuid=True), sa.ForeignKey('chat_groups.id', ondelete='CASCADE'), primary_key=True)
)

class Chat(Base):
    __tablename__ = "chat_chats"
    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True)
    chat_name: Mapped[str] = mapped_column(sa.String(length=255), nullable=False)
    chat_logo: Mapped[str] = mapped_column(sa.String(length=255), nullable=True)
    is_group: Mapped[bool] = mapped_column(sa.Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(sa.TIMESTAMP, server_default=func.now())
    messages = relationship("Message", back_populates="chat")
    users = relationship("User", secondary="chat_chat_users", back_populates="chats")
    histories = relationship("History", back_populates="chat")
    images = relationship("Image", back_populates="chat")

class Group(Base):
    __tablename__ = "chat_groups"
    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True)
    group_name: Mapped[str] = mapped_column(sa.String(length=255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(sa.TIMESTAMP, server_default=func.now())
    members = relationship("User", secondary="chat_user_groups", back_populates="groups")

class BaseChatMessage(Base):
    __abstract__=True
    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True)
    user_id: Mapped[str] = mapped_column(UUID(as_uuid=True), sa.ForeignKey("chat_users.id"), nullable=False)
    chat_id: Mapped[str] = mapped_column(UUID(as_uuid=True), sa.ForeignKey("chat_chats.id"), nullable=False)
    readed: Mapped[bool] = mapped_column(sa.Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(sa.TIMESTAMP, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(sa.TIMESTAMP, server_default=func.now(), onupdate=func.now())
    author = relationship("User", back_populates="messages")
    chat = relationship("Chat", back_populates="messages")

class Message(BaseChatMessage):
    __tablename__ = "chat_messages"
    content: Mapped[str] = mapped_column(sa.String(length=4096), nullable=False)

class Video(BaseChatMessage):
    __tablename__ = "chat_videos"
    content: Mapped[str] = mapped_column(sa.String(length=255), nullable=False)
    description: Mapped[str] = mapped_column(sa.String(length=1024), nullable=True)

class Image(BaseChatMessage):
    __tablename__ = "chat_images"
    content: Mapped[str] = mapped_column(sa.String(length=255), nullable=False)
    description: Mapped[str] = mapped_column(sa.String(length=1024), nullable=True)