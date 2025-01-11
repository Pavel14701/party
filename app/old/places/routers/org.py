from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.infrastructure.database import get_session
from app.places.schemas import OrganizationCreate, Organization
from app.places.crud import (
    create_organization,
    get_organization,
    get_organizations,
    update_organization,
    delete_organization,
)


class OrganisazationRouters:
    """Provides CRUD endpoints for organizations.
    This class defines API endpoints for creating, reading, updating, and deleting organizations.
    """
    router = APIRouter()

    @router.post("/organizations/", response_model=Organization)
    async def create_organization_endpoint(
        self, organization: OrganizationCreate, db: AsyncSession = Depends(get_session)
    ):
        """Creates a new organization.
        Args:
            organization: The organization data to create.
            db: The database session.
        Returns:
            The created organization.
        """
        return await create_organization(db, organization)

    @router.get("/organizations/{organization_id}", response_model=Organization)
    async def read_organization(
        self, organization_id: int, db: AsyncSession = Depends(get_session)
    ):
        """Retrieves an organization by ID.
        Args:
            organization_id: The ID of the organization to retrieve.
            db: The database session.
        Returns:
            The retrieved organization.
        Raises:
            HTTPException: If the organization is not found.
        """
        db_organization = await get_organization(db, organization_id)
        if db_organization is None:
            raise HTTPException(status_code=404, detail="Organization not found")
        return db_organization

    @router.get("/organizations/", response_model=List[Organization])
    async def read_organizations(
        self, skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)
    ):
        """Retrieves a list of organizations.
        Args:
            skip: The number of organizations to skip.
            limit: The maximum number of organizations to return.
            db: The database session.
        Returns:
            A list of organizations.
        """
        return await get_organizations(db, skip, limit)

    @router.put("/organizations/{organization_id}", response_model=Organization)
    async def update_organization_endpoint(
        self,
        organization_id: int,
        organization: OrganizationCreate,
        db: AsyncSession = Depends(get_session),
    ):
        """Updates an existing organization.
        Args:
            organization_id: The ID of the organization to update.
            organization: The updated organization data.
            db: The database session.
        Returns:
            The updated organization.
        Raises:
            HTTPException: If the organization is not found.
        """
        db_organization = await update_organization(db, organization_id, organization)
        if db_organization is None:
            raise HTTPException(status_code=404, detail="Organization not found")
        return db_organization

    @router.delete("/organizations/{organization_id}", response_model=Organization)
    async def delete_organization_endpoint(
        self, organization_id: int, db: AsyncSession = Depends(get_session)
    ):
        """Deletes an organization.
        Args:
            organization_id: The ID of the organization to delete.
            db: The database session.
        Returns:
            The deleted organization.
        Raises:
            HTTPException: If the organization is not found.
        """
        db_organization = await delete_organization(db, organization_id)
        if db_organization is None:
            raise HTTPException(status_code=404, detail="Organization not found")
        return db_organization