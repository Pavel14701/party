from sqlalchemy import (
    Column, Integer, BigInteger,
    String, ForeignKey, Table,
    Numeric
)
from sqlalchemy.orm import (relationship, DeclarativeMeta)
from app.core.base_class import _Base

Base:DeclarativeMeta = _Base()

# Ассоциативные таблицы
association_table_categories = Table(
    "place_association_categories", Base.metadata,
    Column("place_id", ForeignKey("place_places.id"), primary_key=True),
    Column("category_id", ForeignKey("place_categories.id"), primary_key=True)
)

association_table_labels = Table(
    "place_association_labels", Base.metadata,
    Column("place_id", ForeignKey("place_places.id"), primary_key=True),
    Column("label_id", ForeignKey("place_labels.id"), primary_key=True)
)

association_table_organizations = Table(
    "place_association_organizations", Base.metadata,
    Column("place_id", ForeignKey("place_places.id"), primary_key=True),
    Column("organization_id", ForeignKey("place_organization.id"), primary_key=True)
)

# Модели
class Organization(Base):
    __tablename__ = "place_organization"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255))
    unp = Column(String(length=255))
    address = Column(String(length=255))
    current_account = Column(String(length=50))
    latitude = Column(Numeric(9, 6), nullable=False)  # Широта
    longitude = Column(Numeric(9, 6), nullable=False)  # Долгота
    places = relationship("Place", back_populates="organization")

class Place(Base):
    __tablename__ = "place_places"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(length=255), index=True)
    organization_id = Column(Integer, ForeignKey("place_organization.id"))
    organization = relationship("Organization", back_populates="places")
    latitude = Column(Numeric(9, 6), nullable=False)  # Широта
    longitude = Column(Numeric(9, 6), nullable=False)  # Долгота
    description = Column(String(length=4096))
    logo = Column(String(length=255))
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
    id = Column(BigInteger, primary_key=True, index=True)
    reviewer_name = Column(String(length=255))
    review = Column(String(length=255))
    review_mark = Column(Numeric(1, 0))
    place_id = Column(Integer, ForeignKey("place_places.id"))
    place = relationship("Place", back_populates="reviews_google")

class YandexReviews(Base):
    __tablename__ = "place_reviews_yandex"
    id = Column(BigInteger, primary_key=True, index=True)
    reviewer_name = Column(String(length=255))
    review = Column(String(length=255))
    review_mark = Column(Numeric(1, 0))
    place_id = Column(Integer, ForeignKey("place_places.id"))
    place = relationship("Place", back_populates="reviews_yandex")

class Category(Base):
    __tablename__ = "place_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=100))
    places = relationship("Place", secondary=association_table_categories, back_populates="categories")

class Label(Base):
    __tablename__ = "place_labels"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(length=100))
    places = relationship("Place", secondary=association_table_labels, back_populates="labels")

class Image(Base):
    __tablename__ = "place_images"
    id = Column(BigInteger, primary_key=True, index=True)
    alt = Column(String(lenghts=150))
    url = Column(String(length=255))
    place_id = Column(Integer, ForeignKey("place_places.id"))
    place = relationship("Place", back_populates="images")

class Video(Base):
    __tablename__ = "place_videos"
    id = Column(BigInteger, primary_key=True, index=True)
    url = Column(String(length=255))
    place_id = Column(Integer, ForeignKey("place_places.id"))
    place = relationship("Place", back_populates="videos")


class Service(Base):
    __tablename__ = "place_services"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(length=255))
    price = Column(Numeric(7, 2))
    place_id = Column(Integer, ForeignKey("place_places.id"))
    place = relationship("Place", back_populates="services")

class MenuItem(Base):
    __tablename__ = "place_menu_items"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(length=100))
    price = Column(Numeric(7, 2))
    category_id = Column(Integer, ForeignKey("place_menu_categories.id"))
    place_id = Column(Integer, ForeignKey("place_places.id"))
    place = relationship("Place", back_populates="menu_items")
    category = relationship("MenuCategory", back_populates="menu_items")

class MenuCategory(Base):
    __tablename__ = "place_menu_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=100))
    menu_items = relationship("MenuItem", back_populates="category")