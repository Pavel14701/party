from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.infrastructure.database import get_session
from app.places.schemas import (PlaceCreate, Place)
from app.places.crud import (
    create_place, get_place, get_places,
    update_place, delete_place
)


class PlaceRouters:
    """Provides CRUD endpoints for places.

    This class defines API endpoints for creating, reading, updating, and deleting places.
    """

    router = APIRouter()

    @router.post("/places/", response_model=Place)
    async def create_place_endpoint(
        self, place: PlaceCreate, db: AsyncSession = Depends(get_session)
    ):
        """Creates a new place.
        Args:
            place: The place data to create.
            db: The database session.
        Returns:
            The created place.
        """
        return await create_place(db, place)

    @router.get("/places/{place_id}", response_model=Place)
    async def read_place(self, place_id: int, db: AsyncSession = Depends(get_session)):
        """Retrieves a place by ID.
        Args:
            place_id: The ID of the place to retrieve.
            db: The database session.
        Returns:
            The retrieved place.
        Raises:
            HTTPException: If the place is not found.
        """
        db_place = await get_place(db, place_id)
        if db_place is None:
            raise HTTPException(status_code=404, detail="Place not found")
        return db_place

    @router.get("/places/", response_model=List[Place])
    async def read_places(
        self, skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)
    ):
        """Retrieves a list of places.
        Args:
            skip: The number of places to skip.
            limit: The maximum number of places to return.
            db: The database session.
        Returns:
            A list of places.
        """
        return await get_places(db, skip, limit)

    @router.put("/places/{place_id}", response_model=Place)
    async def update_place_endpoint(
        self, place_id: int, place: PlaceCreate, db: AsyncSession = Depends(get_session)
    ):
        """Updates an existing place.
        Args:
            place_id: The ID of the place to update.
            place: The updated place data.
            db: The database session.
        Returns:
            The updated place.
        Raises:
            HTTPException: If the place is not found.
        """
        db_place = await update_place(db, place_id, place)
        if db_place is None:
            raise HTTPException(status_code=404, detail="Place not found")
        return db_place

    @router.delete("/places/{place_id}", response_model=Place)
    async def delete_place_endpoint(
        self, place_id: int, db: AsyncSession = Depends(get_session)
    ):
        """Deletes a place.
        Args:
            place_id: The ID of the place to delete.
            db: The database session.
        Returns:
            The deleted place.
        Raises:
            HTTPException: If the place is not found.
        """
        db_place = await delete_place(db, place_id)
        if db_place is None:
            raise HTTPException(status_code=404, detail="Place not found")
        return db_place