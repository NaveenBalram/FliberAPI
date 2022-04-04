import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.daily_asset_data import (
    OutDailyAssetDataSchema,
    InDailyAssetDataSchema,
    DailyAssetDataSchemaBase,
    DailyAssetDataSchema,
)
from app.service.daily_asset_data import DailyAssetDataService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_daily_asset_data(
    payload: InDailyAssetDataSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save daily asset data."""
    daily_asset_data_service = DailyAssetDataService(db)
    daily_asset_data = await daily_asset_data_service.create(payload)
    return daily_asset_data


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_daily_asset_data(
    payload: DailyAssetDataSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update daily asset data."""
    daily_asset_data_service = DailyAssetDataService(db)
    await daily_asset_data_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_daily_asset_data(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to fetch all daily asset data by id."""
    daily_asset_data_service = DailyAssetDataService(db)
    daily_asset_data = await daily_asset_data_service.get_by_id(uuid)
    return daily_asset_data


@router.get("/", status_code=status.HTTP_200_OK)
async def get_daily_asset_data(db: AsyncSession = Depends(get_db)):
    """ api to fetch all daily asset data."""
    daily_asset_data_service = DailyAssetDataService(db)
    daily_asset_data = await daily_asset_data_service.get_all()
    return daily_asset_data


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_daily_asset_data(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete daily asset data by id."""
    daily_asset_data_service = DailyAssetDataService(db)
    await daily_asset_data_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_corpus_status_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete corpus status data by user id."""
    corpus_status_service = DailyAssetDataService(db)
    return await corpus_status_service.delete_by_user_id(user_id)

