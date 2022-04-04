import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.fund_level_asset_percent import (
    OutFundLevelAssetPercentSchema,
    InFundLevelAssetPercentSchema,
    FundLevelAssetPercentSchemaBase,
    FundLevelAssetPercentSchema,
)
from app.service.fund_level_asset_percent import FundLevelAssetPercentService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_fund_level_asset_percent(
    payload: InFundLevelAssetPercentSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save fund level asset percentage data. """
    fund_level_asset_percent_service = FundLevelAssetPercentService(db)
    fund_level_asset_percent = await fund_level_asset_percent_service.create(payload)
    return fund_level_asset_percent


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_fund_level_asset_percent(
    payload: FundLevelAssetPercentSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update fund level asset percentage data. """
    fund_level_asset_percent_service = FundLevelAssetPercentService(db)
    await fund_level_asset_percent_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_fund_level_asset_percent(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to fetch fund level asset percentage data by id. """
    fund_level_asset_percent_service = FundLevelAssetPercentService(db)
    fund_level_asset_percent = await fund_level_asset_percent_service.get_by_id(uuid)
    return fund_level_asset_percent


@router.get("/", status_code=status.HTTP_200_OK)
async def get_fund_level_asset_percent(db: AsyncSession = Depends(get_db)):
    """ api to fetch all fund level asset percentage data. """
    fund_level_asset_percent_service = FundLevelAssetPercentService(db)
    fund_level_asset_percent = await fund_level_asset_percent_service.get_all()
    return fund_level_asset_percent


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_fund_level_asset_percent(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete fund level asset percentage data by id. """
    fund_level_asset_percent_service = FundLevelAssetPercentService(db)
    await fund_level_asset_percent_service.delete(uuid)
