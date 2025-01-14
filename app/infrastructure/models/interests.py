import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime

from app.core.base_class import Base


# Ассоциация для избранных кухонь
association_table_favorites_cuisines = sa.Table("user_favorites_cuisines", Base.metadata,
    mapped_column("user_id", sa.ForeignKey("user_users.id"), primary_key=True),
    mapped_column("cuisine_id", sa.ForeignKey("user_cuisines.id"), primary_key=True)
)

# Ассоциация для избранных стилей музыки
association_table_favorites_music_styles = sa.Table("user_favorites_music_styles", Base.metadata,
    mapped_column("user_id", sa.ForeignKey("user_users.id"), primary_key=True),
    mapped_column("music_style_id", sa.ForeignKey("user_music_styles.id"), primary_key=True)
)

# Ассоциация для избранных мест
association_table_favorites_places = sa.Table("user_favorites_places", Base.metadata,
    mapped_column("user_id", sa.ForeignKey("user_users.id"), primary_key=True),
    mapped_column("place_id", sa.ForeignKey("user_places.id"), primary_key=True)
)


class Cuisine(Base):
    __tablename__ = "user_cuisines"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(length=255), unique=True, nullable=False, index=True)
    users = relationship(argument="User", secondary=association_table_favorites_cuisines, back_populates="favorite_cuisines")

class MusicStyle(Base):
    __tablename__ = "user_music_styles"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(length=255), unique=True, nullable=False, index=True)
    users = relationship(argument="User", secondary=association_table_favorites_music_styles, back_populates="favorite_music_styles")

class Place(Base):
    __tablename__ = "user_places"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key = True)
    name: Mapped[str] = mapped_column(sa.String(length=255), unique=True, nullable=False, index=True)