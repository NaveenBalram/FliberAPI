import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.asset_type import (
    InAssetTypeSchema,
    AssetTypeSchema,
)
from app.service.asset_type import AssetTypeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_asset_type(
        payload: InAssetTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save asset asset type data. """
    asset_type_service = AssetTypeService(db)
    asset_type = await asset_type_service.create(payload)
    return asset_type


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_asset_type(
        payload: AssetTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update asset asset type data. """
    asset_type_service = AssetTypeService(db)
    await asset_type_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK,
)
async def get_asset_type(
        uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to get asset type data by id. """
    asset_type_service = AssetTypeService(db)
    asset_type = await asset_type_service.get_by_id(uuid)
    return asset_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_asset_type(db: AsyncSession = Depends(get_db)):
    """ api to save asset type data. """
    asset_type_service = AssetTypeService(db)
    asset_type = await asset_type_service.get_all()
    return asset_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_asset_type(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete asset type data by id. """
    asset_type_service = AssetTypeService(db)
    return await asset_type_service.delete(uuid)

