import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.asset_liability_category import (
    OutAssetLiabilityCategorySchema,
    InAssetLiabilityCategorySchema,
    AssetLiabilityCategorySchema,
)
from app.service.asset_liability_category import AssetLiabilityCategoryService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=OutAssetLiabilityCategorySchema,
)
async def create_asset_liability_category(
    payload: InAssetLiabilityCategorySchema, db: AsyncSession = Depends(get_db)
) -> OutAssetLiabilityCategorySchema:
    """ api to save asset liability data. """
    asset_liability_category_service = AssetLiabilityCategoryService(db)
    asset_liability_category = await asset_liability_category_service.create(payload)
    return asset_liability_category


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_asset_liability_category(
    payload: AssetLiabilityCategorySchema, db: AsyncSession = Depends(get_db)
):
    """ api to save asset liability data. """
    asset_liability_category_service = AssetLiabilityCategoryService(db)
    await asset_liability_category_service.update(payload)


@router.get(
    "/{uuid}",
    status_code=status.HTTP_200_OK,
    response_model=OutAssetLiabilityCategorySchema,
)
async def get_asset_liability_category(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch asset liability data by id. """
    asset_liability_category_service = AssetLiabilityCategoryService(db)
    asset_liability_category = await asset_liability_category_service.get_by_id(uuid)
    return asset_liability_category


@router.get("/", status_code=status.HTTP_200_OK)
async def get_asset_liability_category(db: AsyncSession = Depends(get_db)):
    """ api to fetch all asset liability data. """
    asset_liability_category_service = AssetLiabilityCategoryService(db)
    asset_liability_category = await asset_liability_category_service.get_all()
    return asset_liability_category


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_asset_liability_category(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to save asset liability data. """
    asset_liability_category_service = AssetLiabilityCategoryService(db)
    return await asset_liability_category_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_asset_liability_category_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to save asset liability data. """
    asset_liability_category_service = AssetLiabilityCategoryService(db)
    return await asset_liability_category_service.delete(user_id)
