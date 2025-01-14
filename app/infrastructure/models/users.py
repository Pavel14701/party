import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime

from app.core.base_class import Base
from .interests import (
    association_table_favorites_cuisines,
    association_table_favorites_music_styles,
    association_table_favorites_places
)

class User(Base):
    __tablename__ = "user_users"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True)
    is_superuser: Mapped[bool] = mapped_column(sa.Boolean)
    username: Mapped[str] = mapped_column(sa.String(length=255), unique=True, nullable=False, index=True)
    firstname: Mapped[str] = mapped_column(sa.String(length=50), nullable=True)
    lastname: Mapped[str] = mapped_column(sa.String(length=50), nullable=True)
    email: Mapped[str] = mapped_column(sa.String(length=255), unique=True, nullable=True, index=True)
    organization: Mapped = mapped_column(sa.String, sa.ForeignKey("place_organization.id"), nullable=True)
    password: Mapped[str] = mapped_column(sa.String(length=1024))
    country_id: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey("user_countries.id"))
    country = relationship("Country")
    bio: Mapped[str] = mapped_column(sa.String(length=2048), nullable=True)
    phone_number: Mapped[str] = mapped_column(sa.String(length=30), unique=True, nullable=False, index=True)
    favorite_cuisines = relationship(argument="Cuisine", secondary=association_table_favorites_cuisines, back_populates="users")
    favorite_music_styles = relationship(argument="MusicStyle", secondary=association_table_favorites_music_styles, back_populates="users")
    favorite_places = relationship(argument="Place", secondary=association_table_favorites_places, back_populates="users")
    groups = relationship(argument="Group", secondary="chat_user_groups", back_populates="members")
    messages = relationship(argument="Message", back_populates="author")
    histories = relationship(argument="History", back_populates="author")
    images = relationship(argument="Image", back_populates="author")
    created_at: Mapped[datetime] = mapped_column(sa.TIMESTAMP, server_default=func.now())

class Country(Base):
    __tablename__ = "user_countries"
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(length=150), unique=True, nullable=False, index=True)
    code: Mapped[str] = mapped_column(sa.String(length=10), unique=True, nullable=False)

