import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime

from app.core.base_class import Base


# Ассоциация для избранных кухонь
association_table_favorites_cuisines = sa.Table(
    "user_favorites_cuisines", Base.metadata,
    mapped_column("user_id", sa.ForeignKey("user_users.id"), primary_key=True),
    mapped_column("cuisine_id", sa.ForeignKey("user_cuisines.id"), primary_key=True)
)

# Ассоциация для избранных стилей музыки
association_table_favorites_music_styles = sa.Table(
    "user_favorites_music_styles", Base.metadata,
    mapped_column("user_id", sa.ForeignKey("user_users.id"), primary_key=True),
    mapped_column("music_style_id", sa.ForeignKey("user_music_styles.id"), primary_key=True)
)

# Ассоциация для избранных мест
association_table_favorites_places = sa.Table(
    "user_favorites_places", Base.metadata,
    mapped_column("user_id", sa.ForeignKey("user_users.id"), primary_key=True),
    mapped_column("place_id", sa.ForeignKey("user_places.id"), primary_key=True)
)

class User(Base):
    __tablename__ = "user_users"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String(length=255), unique=True, nullable=False, index=True)
    firstname: Mapped[str] = mapped_column(sa.String(length=50))
    lastname: Mapped[str] = mapped_column(sa.String(length=50))
    email: Mapped[str] = mapped_column(sa.String(length=255), unique=True, nullable=True)
    password: Mapped[str] = mapped_column(sa.String(length=1024))
    country_id: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey("user_countries.id"))
    country = relationship("Country")
    bio: Mapped[str] = mapped_column(sa.String(length=2048))
    phone_number: Mapped[str] = mapped_column(sa.String(length=30), unique=True, nullable=False, index=True)
    favorite_cuisines = relationship("Cuisine", secondary=association_table_favorites_cuisines, back_populates="users")
    favorite_music_styles = relationship("MusicStyle", secondary=association_table_favorites_music_styles, back_populates="users")
    favorite_places = relationship("Place", secondary=association_table_favorites_places, back_populates="users")
    groups = relationship("Group", secondary="chat_user_groups", back_populates="members")
    messages = relationship("Message", back_populates="author")
    histories = relationship("History", back_populates="author")
    images = relationship("Image", back_populates="author")
    created_at: Mapped[datetime] = mapped_column(sa.TIMESTAMP, server_default=func.now())

class Country(Base):
    __tablename__ = "user_countries"
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(length=150), unique=True, nullable=False, index=True)
    code: Mapped[str] = mapped_column(sa.String(length=10), unique=True, nullable=False)

class Cuisine(Base):
    __tablename__ = "user_cuisines"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(length=255), unique=True, nullable=False, index=True)
    users = relationship("User", secondary=association_table_favorites_cuisines, back_populates="favorite_cuisines")

class MusicStyle(Base):
    __tablename__ = "user_music_styles"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(length=255), unique=True, nullable=False, index=True)
    users = relationship("User", secondary=association_table_favorites_music_styles, back_populates="favorite_music_styles")

class Place(Base):
    __tablename__ = "user_places"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(length=255), unique=True, nullable=False, index=True)