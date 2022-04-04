import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.areas_of_concerns import (
    OutAreasOfConcernsSchema,
    InAreasOfConcernsSchema,
    AreasOfConcernsSchema,
)
from app.service.areas_of_concerns import AreasOfConcernsService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_areas_of_concerns(
    payload: InAreasOfConcernsSchema, db: AsyncSession = Depends(get_db)
):
    """Api to save data."""
    try:
        areas_of_concerns_service = AreasOfConcernsService(db)
        areas_of_concerns = await areas_of_concerns_service.create(payload)
        return areas_of_concerns
    except Exception as e:
        return {"error": str(e)}


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_areas_of_concerns(
    payload: AreasOfConcernsSchema, db: AsyncSession = Depends(get_db)
):
    """Api to update data."""
    try:
        areas_of_concerns_service = AreasOfConcernsService(db)
        await areas_of_concerns_service.update(payload)
    except Exception as e:
        return {"error": str(e)}


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_areas_of_concerns(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """Api to fetch data by id."""
    try:
        areas_of_concerns_service = AreasOfConcernsService(db)
        areas_of_concerns = await areas_of_concerns_service.get_by_id(uuid)
        return areas_of_concerns
    except Exception as e:
        return {"error": str(e)}


@router.get("/", status_code=status.HTTP_200_OK)
async def get_areas_of_concerns(db: AsyncSession = Depends(get_db)):
    """Api to fetch areas of concern data."""
    try:
        areas_of_concerns_service = AreasOfConcernsService(db)
        areas_of_concerns = await areas_of_concerns_service.get_all()
        return areas_of_concerns
    except Exception as e:
        return {"error": str(e)}


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_areas_of_concerns(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """Api to delete data using id."""
    try:
        areas_of_concerns_service = AreasOfConcernsService(db)
        return await areas_of_concerns_service.delete(uuid)
    except Exception as e:
        return {"error": str(e)}
