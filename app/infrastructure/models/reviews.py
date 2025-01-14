from decimal import Decimal

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from app.core.base_class import Base

class ReviewsBase(Base):
    __abstract__ = True
    id: Mapped[str] = mapped_column(sa.Uuid, primary_key=True)
    reviewer_name: Mapped[str] = mapped_column(sa.String(length=255), index=True)
    review: Mapped[str] = mapped_column(sa.String(length=2048))
    review_mark: Mapped[Decimal] = mapped_column(sa.Numeric(1, 2))
    place_id: Mapped[str] = mapped_column(sa.Uuid, sa.ForeignKey("place_places.id"))

class GoogleReviews(ReviewsBase):
    __tablename__ = "place_reviews_google"
    place = relationship("Place", back_populates="reviews_google")

class YandexReviews(ReviewsBase):
    __tablename__ = "place_reviews_yandex"
    place = relationship("Place", back_populates="reviews_yandex")

class Reviews(ReviewsBase):
    __tablename__ = "place_reviews"
    reviewer_name: Mapped[str] = mapped_column(sa.String(length=255), sa.ForeignKey("user_users.username"), index=True)
    reviewer_id: Mapped[str] = mapped_column(sa.Uuid, sa.ForeignKey("user_users.id"))
    place = relationship("Place", back_populates="reviews")