from decimal import Decimal
from datetime import datetime
import sqlalchemy as sa
from geoalchemy2 import Geography
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.core.base_class import Base
from datetime import time
import enum

# Ассоциативные таблицы
association_table_categories = sa.Table(
    "place_association_categories", Base.metadata,
    sa.Column("place_id", sa.ForeignKey("place_places.id"), primary_key=True),
    sa.Column("category_id", sa.ForeignKey("place_categories.id"), primary_key=True)
)

association_table_labels = sa.Table(
    "place_association_labels", Base.metadata,
    sa.Column("place_id", sa.ForeignKey("place_places.id"), primary_key=True),
    sa.Column("label_id", sa.ForeignKey("place_labels.id"), primary_key=True)
)

association_table_organizations = sa.Table(
    "place_association_organizations", Base.metadata,
    sa.Column("place_id", sa.ForeignKey("place_places.id"), primary_key=True),
    sa.Column("organization_id", sa.ForeignKey("place_organization.id"), primary_key=True)
)

# Модели
class Organization(Base):
    __tablename__ = "place_organization"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(sa.String(length=255), index=True)
    unp: Mapped[str]= mapped_column(sa.String(length=255))
    address: Mapped[str] = mapped_column(sa.String(length=255))
    current_account: Mapped[str] = mapped_column(sa.String(length=50)) # Рассчётный счёт
    latitude: Mapped[Decimal] = mapped_column(sa.Numeric(9, 6), nullable=False)  # Широта
    longitude: Mapped[Decimal] = mapped_column(sa.Numeric(9, 6), nullable=False)  # Долгота
    places = relationship("Place", back_populates="organization")

class Place(Base):
    __tablename__ = "place_places"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(sa.String(length=255), index=True)
    organization_id: Mapped[str] = mapped_column(sa.Uuid, sa.ForeignKey("place_organization.id"))
    organization = relationship("Organization", back_populates="places")
    latitude: Mapped[Decimal] = mapped_column(sa.Numeric(9, 6), nullable=False)  # Широта
    longitude: Mapped[Decimal] = mapped_column(sa.Numeric(9, 6), nullable=False)  # Долгота
    geom: Mapped[str] = mapped_column(Geography(geometry_type='POINT', srid=4326)) # Поле для PostGIS
    description: Mapped[str] = mapped_column(sa.String(length=4096))
    logo: Mapped[str] = mapped_column(sa.String(length=255))
    videos = relationship("Video", back_populates="place")
    images = relationship("Image", back_populates="place")
    services = relationship("Service", back_populates="place")
    menu_items = relationship("MenuItem", back_populates="place")
    categories = relationship("Category", secondary=association_table_categories, back_populates="place")
    labels = relationship("Label", secondary=association_table_labels, back_populates="place")
    reviews_google = relationship("GoogleReviews", back_populates="place")
    reviews_yandex = relationship("YandexReviews", back_populates="place")

class GoogleReviews(Base):
    __tablename__ = "place_reviews_google"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True)
    reviewer_name: Mapped[str] = mapped_column(sa.String(length=255), index=True)
    review: Mapped[str] = mapped_column(sa.String(length=2048))
    review_mark: Mapped[Decimal] = mapped_column(sa.Numeric(1, 2))
    place_id: Mapped[str] = mapped_column(sa.Uuid, sa.ForeignKey("place_places.id"))
    place = relationship("Place", back_populates="reviews_google")

class YandexReviews(Base):
    __tablename__ = "place_reviews_yandex"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True)
    reviewer_name: Mapped[str] = mapped_column(sa.String(length=255), index=True)
    review: Mapped[str] = mapped_column(sa.String(length=255))
    review_mark: Mapped[Decimal] = mapped_column(sa.Numeric(1, 0))
    place_id: Mapped[str] = mapped_column(sa.Uuid, sa.ForeignKey("place_places.id"))
    place = relationship("Place", back_populates="reviews_yandex")

class Category(Base):
    __tablename__ = "place_categories"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(length=128), index=True)
    places = relationship("Place", secondary=association_table_categories, back_populates="categories")

class Label(Base):
    __tablename__ = "place_labels"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(sa.String(length=100))
    places = relationship("Place", secondary=association_table_labels, back_populates="labels")

class Image(Base):
    __tablename__ = "place_images"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True, index=True, autoincrement="auto")
    alt: Mapped[str] = mapped_column(sa.String(length=150))
    url: Mapped[str] = mapped_column(sa.String(length=255))
    place_id: Mapped[str] = mapped_column(sa.Uuid, sa.ForeignKey("place_places.id"))
    place = relationship("Place", back_populates="images")

class Video(Base):
    __tablename__ = "place_videos"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True, index=True)
    url: Mapped[str] = mapped_column(sa.String(length=255))
    place_id: Mapped[str] = mapped_column(sa.Uuid, sa.ForeignKey("place_places.id"))
    place = relationship("Place", back_populates="videos")


class Service(Base):
    __tablename__ = "place_services"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(length=255), index=True)
    price: Mapped[Decimal] = mapped_column(sa.Numeric(7, 2))
    place_id: Mapped[str] = mapped_column(sa.Uuid, sa.ForeignKey("place_places.id"))
    place = relationship("Place", back_populates="services")

class MenuItem(Base):
    __tablename__ = "place_menu_items"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(length=100), index=True)
    price: Mapped[Decimal] = mapped_column(sa.Numeric(5, 2))
    category_id: Mapped[str] = mapped_column(sa.Uuid, sa.ForeignKey("place_menu_categories.id"))
    place_id: Mapped[str] = mapped_column(sa.Uuid, sa.ForeignKey("place_places.id"))
    place = relationship("Place", back_populates="menu_items")
    category = relationship("MenuCategory", back_populates="menu_items")

class MenuCategory(Base):
    __tablename__ = "place_menu_categories"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True, index=True, autoincrement="auto")
    name: Mapped[str] = mapped_column(sa.String(length=100))
    menu_items = relationship("MenuItem", back_populates="category")

class DayOfWeek(enum.Enum):
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
    Saturday = "Saturday"
    Sunday = "Sunday"

class PlaceHours(Base):
    __tablename__ = "place_hours"
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True, index=True)
    day_of_week = mapped_column(sa.Enum(DayOfWeek), nullable=False)
    open_time: Mapped[datetime] = mapped_column(sa.Time, nullable=False, default=time(9, 0))
    close_time: Mapped[datetime] = mapped_column(sa.Time, nullable=False, default=time(18, 0))
    is_weekend: Mapped[bool] = mapped_column(sa.Boolean, default=False, nullable=False)
    place_id: Mapped[str] = mapped_column(sa.Uuid, sa.ForeignKey('place_places.id'))
    comment: Mapped[str] = mapped_column(sa.String(length=255), nullable=True)
    place = relationship("Place", back_populates="hours")