import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.daily_nav_data import (
    OutDailyNavDataSchema,
    InDailyNavDataSchema,
    DailyNavDataSchemaBase,
    DailyNavDataSchema,
)
from app.service.daily_nav_data import DailyNavDataService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_daily_nav_data(
    payload: InDailyNavDataSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save daily nav data"""
    daily_nav_data_service = DailyNavDataService(db)
    daily_nav_data = await daily_nav_data_service.create(payload)
    return daily_nav_data


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_daily_nav_data(
    payload: DailyNavDataSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update daily nav data."""
    daily_nav_data_service = DailyNavDataService(db)
    await daily_nav_data_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_daily_nav_data(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to fetch daily nav data by id."""
    daily_nav_data_service = DailyNavDataService(db)
    daily_nav_data = await daily_nav_data_service.get_by_id(uuid)
    return daily_nav_data


@router.get("/", status_code=status.HTTP_200_OK)
async def get_daily_nav_data(db: AsyncSession = Depends(get_db)):
    """ api to fetch all daily nav data"""
    daily_nav_data_service = DailyNavDataService(db)
    daily_nav_data = await daily_nav_data_service.get_all()
    return daily_nav_data


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_daily_nav_data(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete daily nav data by id"""
    daily_nav_data_service = DailyNavDataService(db)
    await daily_nav_data_service.delete(uuid)
