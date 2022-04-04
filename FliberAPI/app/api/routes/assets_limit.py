import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.assets_limit import (
    OutAssetsLimitSchema,
    InAssetsLimitSchema,
    AssetsLimitSchemaBase,
    AssetsLimitSchema,
)
from app.service.assets_limit import AssetsLimitService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_assets_limit(
    payload: InAssetsLimitSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save asset limit type data. """
    assets_limit_service = AssetsLimitService(db)
    assets_limit = await assets_limit_service.create(payload)
    return assets_limit


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_assets_limit(
    payload: AssetsLimitSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update asset limit type data. """
    assets_limit_service = AssetsLimitService(db)
    await assets_limit_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_assets_limit(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to fetch asset limit type data by id. """
    assets_limit_service = AssetsLimitService(db)
    assets_limit = await assets_limit_service.get_by_id(uuid)
    return assets_limit


@router.get("/", status_code=status.HTTP_200_OK)
async def get_assets_limit(db: AsyncSession = Depends(get_db)):
    """ api to fetch all asset limit type data. """
    assets_limit_service = AssetsLimitService(db)
    assets_limit = await assets_limit_service.get_all()
    return assets_limit


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_assets_limit(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete asset limit type data by id. """
    assets_limit_service = AssetsLimitService(db)
    await assets_limit_service.delete(uuid)
