from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, DeclarativeMeta
from app.db.base_class import _Base

Base:DeclarativeMeta = _Base()

# Префикс place_ для всех таблиц
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

class Place(Base):
    __tablename__ = "place_places"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    logo = Column(String)
    video = Column(String)
    images = relationship("Image", back_populates="place")
    services = relationship("Service", back_populates="place")
    menu_items = relationship("MenuItem", back_populates="place")
    categories = relationship("Category", secondary=association_table_categories, back_populates="places")
    labels = relationship("Label", secondary=association_table_labels, back_populates="places")

class Category(Base):
    __tablename__ = "place_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    places = relationship("Place", secondary=association_table_categories, back_populates="categories")

class Label(Base):
    __tablename__ = "place_labels"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    places = relationship("Place", secondary=association_table_labels, back_populates="labels")

class Image(Base):
    __tablename__ = "place_images"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    place_id = Column(Integer, ForeignKey("place_places.id"))
    place = relationship("Place", back_populates="images")

class Service(Base):
    __tablename__ = "place_services"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    place_id = Column(Integer, ForeignKey("place_places.id"))
    place = relationship("Place", back_populates="services")

class MenuItem(Base):
    __tablename__ = "place_menu_items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey("place_menu_categories.id"))
    place_id = Column(Integer, ForeignKey("place_places.id"))
    place = relationship("Place", back_populates="menu_items")
    category = relationship("MenuCategory", back_populates="menu_items")

class MenuCategory(Base):
    __tablename__ = "place_menu_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    menu_items = relationship("MenuItem", back_populates="category")
