import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.asset_class_hierarchy import (
    OutAssetClassHierarchySchema,
    InAssetClassHierarchySchema,
    AssetClassHierarchySchema
)
from app.service.asset_class_hierarchy import AssetClassHierarchyService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_asset_class_hierarchy(
    payload: InAssetClassHierarchySchema, db: AsyncSession = Depends(get_db)
):
    """ api to save rule asset allocation data. """
    asset_class_hierarchy_service = AssetClassHierarchyService(db)
    asset_class_hierarchy_service = await asset_class_hierarchy_service.create(payload)
    return asset_class_hierarchy_service


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_rule_asset_allocation(
    payload:AssetClassHierarchySchema , db: AsyncSession = Depends(get_db)
):
    """ api to update rule asset allocation  data. """
    asset_class_hierarchy_service = AssetClassHierarchyService(db)
    await asset_class_hierarchy_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_rule_asset_allocation_by_id(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to fetch all rule asset data. """
    asset_class_hierarchy_service = AssetClassHierarchyService(db)
    asset_class_hierarchy_service = await asset_class_hierarchy_service.get_by_id(uuid)
    return asset_class_hierarchy_service


@router.get("/", status_code=status.HTTP_200_OK)
async def get_asset_class_hierarchy(db: AsyncSession = Depends(get_db)):
    """ api to fetch all rule asset data. """
    asset_class_hierarchy_service = AssetClassHierarchyService(db)
    asset_class_hierarchy_service = await asset_class_hierarchy_service.get_all()
    return asset_class_hierarchy_service


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_rule_asset_allocation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to Fetch data by id. """
    asset_class_hierarchy_service = AssetClassHierarchyService(db)
    return await asset_class_hierarchy_service.delete(uuid)

