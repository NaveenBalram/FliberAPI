import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.target_assets import (
    OutTargetAssetsSchema,
    InTargetAssetsSchema,
    TargetAssetsSchema,
)
from app.service.target_assets import TargetAssetsService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutTargetAssetsSchema
)
async def create_target_assets(
    payload: InTargetAssetsSchema, db: AsyncSession = Depends(get_db)
) -> OutTargetAssetsSchema:
    """ api to save target assets data. """
    target_assets_service = TargetAssetsService(db)
    target_assets = await target_assets_service.create(payload)
    return target_assets


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_target_assets(
    payload: TargetAssetsSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update target assets data. """
    target_assets_service = TargetAssetsService(db)
    await target_assets_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutTargetAssetsSchema
)
async def get_target_assets(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutTargetAssetsSchema:
    """ api to get target assets data by id. """
    target_assets_service = TargetAssetsService(db)
    target_assets = await target_assets_service.get_by_id(uuid)
    return target_assets


@router.get("/", status_code=status.HTTP_200_OK)
async def get_target_assets(db: AsyncSession = Depends(get_db)):
    """ api to get target assets data. """
    target_assets_service = TargetAssetsService(db)
    target_assets = await target_assets_service.get_all()
    return target_assets


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_target_assets(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete target assets data by id. """
    target_assets_service = TargetAssetsService(db)
    await target_assets_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_target_assets_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete target assets data by user id. """
    target_assets_service = TargetAssetsService(db)
    await target_assets_service.delete(user_id)
