from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.infrastructure.database import get_session
from app.places.schemas import (
    GoogleReviewsCreate, GoogleReviews,
    YandexReviewsCreate, YandexReviews,
)
from app.places.crud import (
    create_google_review, get_google_review, get_google_reviews,
    update_google_review, delete_google_review,
    create_yandex_review, get_yandex_review, get_yandex_reviews,
    update_yandex_review, delete_yandex_review,
)


class GoogleReviews:
    """Provides CRUD endpoints for Google reviews.
    This class defines API endpoints for creating, reading, updating, and deleting Google reviews.
    """

    router = APIRouter()

    @router.post("/google_reviews/", response_model=GoogleReviews)
    async def create_google_review_endpoint(
        self, review: GoogleReviewsCreate, db: AsyncSession = Depends(get_session)
    ):
        """Creates a new Google review.
        Args:
            review: The Google review data to create.
            db: The database session.
        Returns:
            The created Google review.
        """
        return await create_google_review(db, review)

    @router.get("/google_reviews/{review_id}", response_model=GoogleReviews)
    async def read_google_review(
        self, review_id: int, db: AsyncSession = Depends(get_session)
    ):
        """Retrieves a Google review by ID.
        Args:
            review_id: The ID of the Google review to retrieve.
            db: The database session.
        Returns:
            The retrieved Google review.
        Raises:
            HTTPException: If the Google review is not found.
        """
        db_review = await get_google_review(db, review_id)
        if db_review is None:
            raise HTTPException(status_code=404, detail="Google review not found")
        return db_review

    @router.get("/google_reviews/", response_model=List[GoogleReviews])
    async def read_google_reviews(
        self, skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)
    ):
        """Retrieves a list of Google reviews.
        Args:
            skip: The number of reviews to skip.
            limit: The maximum number of reviews to return.
            db: The database session.
        Returns:
            A list of Google reviews.
        """
        return await get_google_reviews(db, skip, limit)

    @router.put("/google_reviews/{review_id}", response_model=GoogleReviews)
    async def update_google_review_endpoint(
        self, review_id: int, review: GoogleReviewsCreate, db: AsyncSession = Depends(get_session)
    ):
        """Updates an existing Google review.
        Args:
            review_id: The ID of the Google review to update.
            review: The updated Google review data.
            db: The database session.
        Returns:
            The updated Google review.
        Raises:
            HTTPException: If the Google review is not found.
        """
        db_review = await update_google_review(db, review_id, review)
        if db_review is None:
            raise HTTPException(status_code=404, detail="Google review not found")
        return db_review

    @router.delete("/google_reviews/{review_id}", response_model=GoogleReviews)
    async def delete_google_review_endpoint(
        self, review_id: int, db: AsyncSession = Depends(get_session)
    ):
        """Deletes a Google review.
        Args:
            review_id: The ID of the Google review to delete.
            db: The database session.
        Returns:
            The deleted Google review.
        Raises:
            HTTPException: If the Google review is not found.
        """
        db_review = await delete_google_review(db, review_id)
        if db_review is None:
            raise HTTPException(status_code=404, detail="Google review not found")
        return db_review


class YandexReviews:
    """Provides CRUD endpoints for Yandex reviews.
    This class defines API endpoints for creating, reading, updating, and deleting Yandex reviews.
    """
    router = APIRouter()

    @router.post("/yandex_reviews/", response_model=YandexReviews)
    async def create_yandex_review_endpoint(
        self, review: YandexReviewsCreate, db: AsyncSession = Depends(get_session)
    ):
        """Creates a new Yandex review.
        Args:
            review: The Yandex review data to create.
            db: The database session.
        Returns:
            The created Yandex review.
        """
        return await create_yandex_review(db, review)

    @router.get("/yandex_reviews/{review_id}", response_model=YandexReviews)
    async def read_yandex_review(
        self, review_id: int, db: AsyncSession = Depends(get_session)
    ):
        """Retrieves a Yandex review by ID.
        Args:
            review_id: The ID of the Yandex review to retrieve.
            db: The database session.
        Returns:
            The retrieved Yandex review.
        Raises:
            HTTPException: If the Yandex review is not found.
        """
        db_review = await get_yandex_review(db, review_id)
        if db_review is None:
            raise HTTPException(status_code=404, detail="Yandex review not found")
        return db_review

    @router.get("/yandex_reviews/", response_model=List[YandexReviews])
    async def read_yandex_reviews(
        self, skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)
    ):
        """Retrieves a list of Yandex reviews.
        Args:
            skip: The number of reviews to skip.
            limit: The maximum number of reviews to return.
            db: The database session.
        Returns:
            A list of Yandex reviews.
        """
        return await get_yandex_reviews(db, skip, limit)

    @router.put("/yandex_reviews/{review_id}", response_model=YandexReviews)
    async def update_yandex_review_endpoint(
        self,
        review_id: int,
        review: YandexReviewsCreate,
        db: AsyncSession = Depends(get_session),
    ):
        """Updates an existing Yandex review.
        Args:
            review_id: The ID of the Yandex review to update.
            review: The updated Yandex review data.
            db: The database session.
        Returns:
            The updated Yandex review.
        Raises:
            HTTPException: If the Yandex review is not found.
        """
        db_review = await update_yandex_review(db, review_id, review)
        if db_review is None:
            raise HTTPException(status_code=404, detail="Yandex review not found")
        return db_review

    @router.delete("/yandex_reviews/{review_id}", response_model=YandexReviews)
    async def delete_yandex_review_endpoint(
        self, review_id: int, db: AsyncSession = Depends(get_session)
    ):
        """Deletes a Yandex review.
        Args:
            review_id: The ID of the Yandex review to delete.
            db: The database session.
        Returns:
            The deleted Yandex review.
        Raises:
            HTTPException: If the Yandex review is not found.
        """
        db_review = await delete_yandex_review(db, review_id)
        if db_review is None:
            raise HTTPException(status_code=404, detail="Yandex review not found")
        return db_review