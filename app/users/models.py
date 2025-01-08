from sqlalchemy import (
    Column, Integer, BigInteger,
    String, ForeignKey, Table,
    TIMESTAMP
)
from sqlalchemy.orm import (relationship, DeclarativeMeta)
from sqlalchemy.sql import func
from app.core.base_class import _Base

Base:DeclarativeMeta = _Base()


# Ассоциация для избранных кухонь
association_table_favorites_cuisines = Table(
    "user_favorites_cuisines", Base.metadata,
    Column("user_id", ForeignKey("user_users.id"), primary_key=True),
    Column("cuisine_id", ForeignKey("user_cuisines.id"), primary_key=True)
)

# Ассоциация для избранных стилей музыки
association_table_favorites_music_styles = Table(
    "user_favorites_music_styles", Base.metadata,
    Column("user_id", ForeignKey("user_users.id"), primary_key=True),
    Column("music_style_id", ForeignKey("user_music_styles.id"), primary_key=True)
)

# Ассоциация для избранных мест
association_table_favorites_places = Table(
    "user_favorites_places", Base.metadata,
    Column("user_id", ForeignKey("user_users.id"), primary_key=True),
    Column("place_id", ForeignKey("user_places.id"), primary_key=True)
)

class User(Base):
    __tablename__ = "user_users"
    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(length=255), unique=True, nullable=False)
    email = Column(String(length=255), unique=True, nullable=True)
    password = Column(String(length=1024))
    country_id = Column(Integer, ForeignKey("user_countries.id"))
    country = relationship("Country")
    bio = Column(String(lenghts=2048))
    phone_number = Column(String(lenghts=30), unique=True, nullable=False)
    favorite_cuisines = relationship("Cuisine", secondary=association_table_favorites_cuisines, back_populates="users")
    favorite_music_styles = relationship("MusicStyle", secondary=association_table_favorites_music_styles, back_populates="users")
    favorite_places = relationship("Place", secondary=association_table_favorites_places, back_populates="users")
    groups = relationship("Group", secondary="chat_user_groups", back_populates="members")
    messages = relationship("Message", back_populates="author")
    histories = relationship("History", back_populates="author")
    images = relationship("Image", back_populates="author")
    created_at = Column(TIMESTAMP, server_default=func.now())

class Country(Base):
    __tablename__ = "user_countries"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=150), unique=True, nullable=False)
    code = Column(String(length=10), unique=True, nullable=False)

class Cuisine(Base):
    __tablename__ = "user_cuisines"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(length=255), unique=True, nullable=False)
    users = relationship("User", secondary=association_table_favorites_cuisines, back_populates="favorite_cuisines")

class MusicStyle(Base):
    __tablename__ = "user_music_styles"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(length=255), unique=True, nullable=False)
    users = relationship("User", secondary=association_table_favorites_music_styles, back_populates="favorite_music_styles")

class Place(Base):
    __tablename__ = "user_places"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(length=255), unique=True, nullable=False)
    users = relationship("User", secondary=association_table_favorites_places, back_populates="favorite_places")