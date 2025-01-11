from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.infrastructure.database import get_session
from app.places.schemas import CategoryCreate, Category
from app.places.crud import (
    create_category,
    get_category,
    get_categories,
    update_category,
    delete_category,
)


class PlaceCategoriesRouters:
    """Provides CRUD endpoints for categories.
    This class defines API endpoints for creating, reading, updating, and deleting categories.
    """
    router = APIRouter()

    @router.post("/categories/", response_model=Category)
    async def create_category_endpoint(
        self, category: CategoryCreate, db: AsyncSession = Depends(get_session)
    ):
        """Creates a new category.
        Args:
            category: The category data to create.
            db: The database session.
        Returns:
            The created category.
        """
        return await create_category(db, category)

    @router.get("/categories/{category_id}", response_model=Category)
    async def read_category(self, category_id: int, db: AsyncSession = Depends(get_session)):
        """Retrieves a category by ID.
        Args:
            category_id: The ID of the category to retrieve.
            db: The database session.
        Returns:
            The retrieved category.
        Raises:
            HTTPException: If the category is not found.
        """
        db_category = await get_category(db, category_id)
        if db_category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        return db_category

    @router.get("/categories/", response_model=List[Category])
    async def read_categories(
        self, skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)
    ):
        """Retrieves a list of categories.
        Args:
            skip: The number of categories to skip.
            limit: The maximum number of categories to return.
            db: The database session.
        Returns:
            A list of categories.
        """
        return await get_categories(db, skip, limit)

    @router.put("/categories/{category_id}", response_model=Category)
    async def update_category_endpoint(
        self, category_id: int, category: CategoryCreate, db: AsyncSession = Depends(get_session)
    ):
        """Updates an existing category.
        Args:
            category_id: The ID of the category to update.
            category: The updated category data.
            db: The database session.
        Returns:
            The updated category.
        Raises:
            HTTPException: If the category is not found.
        """
        db_category = await update_category(db, category_id, category)
        if db_category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        return db_category

    @router.delete("/categories/{category_id}", response_model=Category)
    async def delete_category_endpoint(
        self, category_id: int, db: AsyncSession = Depends(get_session)
    ):
        """Deletes a category.
        Args:
            category_id: The ID of the category to delete.
            db: The database session.
        Returns:
            The deleted category.
        Raises:
            HTTPException: If the category is not found.
        """
        db_category = await delete_category(db, category_id)
        if db_category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        return db_category