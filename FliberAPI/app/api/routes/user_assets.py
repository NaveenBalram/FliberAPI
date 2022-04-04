import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.user_assets import (
    OutUserAssetsSchema,
    InUserAssetsSchema,
    UserAssetsSchemaBase,
    UserAssetsSchema,
)
from app.service.user_assets import UserAssetsService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user_assets(
    payload: InUserAssetsSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save user assets data. """
    user_assets_service = UserAssetsService(db)
    user_assets = await user_assets_service.create(payload)
    return user_assets


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_user_assets(
    payload: UserAssetsSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update user assets data. """
    user_assets_service = UserAssetsService(db)
    await user_assets_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_user_assets(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to get user assets data by id. """
    user_assets_service = UserAssetsService(db)
    user_assets = await user_assets_service.get_by_id(uuid)
    return user_assets


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user_assets(db: AsyncSession = Depends(get_db)):
    """ api to get user assets data. """
    user_assets_service = UserAssetsService(db)
    user_assets = await user_assets_service.get_all()
    return user_assets


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_user_assets(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete user assets data by id. """
    user_assets_service = UserAssetsService(db)
    await user_assets_service.delete(uuid)
