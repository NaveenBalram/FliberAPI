import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.asset_allocation_attributes import (
    OutAssetAllocationAttributesSchema,
    InAssetAllocationAttributesSchema,
    AssetAllocationAttributesSchemaBase,
    AssetAllocationAttributesSchema,
)
from app.service.asset_allocation_attributes import AssetAllocationAttributesService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_asset_allocation_attributes(
    payload: InAssetAllocationAttributesSchema, db: AsyncSession = Depends(get_db)
):

    try:
        asset_allocation_attributes_service = AssetAllocationAttributesService(db)
        asset_allocation_attributes = await asset_allocation_attributes_service.create(
            payload
        )
        return asset_allocation_attributes
    except Exception as e:
        return {"error": str(e)}


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_asset_allocation_attributes(
    payload: AssetAllocationAttributesSchema, db: AsyncSession = Depends(get_db)
):
    try:
        asset_allocation_attributes_service = AssetAllocationAttributesService(db)
        await asset_allocation_attributes_service.update(payload)
    except Exception as e:
        return {"error": str(e)}


@router.get(
    "/{uuid}",
    status_code=status.HTTP_200_OK,
)
async def get_asset_allocation_attributes(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    try:
        asset_allocation_attributes_service = AssetAllocationAttributesService(db)
        asset_allocation_attributes = (
            await asset_allocation_attributes_service.get_by_id(uuid)
        )
        return asset_allocation_attributes
    except Exception as e:
        return {"error": str(e)}


@router.get("/", status_code=status.HTTP_200_OK)
async def get_asset_allocation_attributes(db: AsyncSession = Depends(get_db)):
    try:
        asset_allocation_attributes_service = AssetAllocationAttributesService(db)
        asset_allocation_attributes = await asset_allocation_attributes_service.get_all()
        return asset_allocation_attributes
    except Exception as e:
        return {"error": str(e)}


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_asset_allocation_attributes(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    try:
        asset_allocation_attributes_service = AssetAllocationAttributesService(db)
        return await asset_allocation_attributes_service.delete(uuid)
    except Exception as e:
        return {"error": str(e)}


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_asset_allocation_attributes_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    try:
        asset_allocation_attributes_service = AssetAllocationAttributesService(db)
        return await asset_allocation_attributes_service.delete(user_id)

    except Exception as e:
        return {"error": str(e)}
