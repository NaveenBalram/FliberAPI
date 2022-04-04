import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.rule_asset_allocation import (
    OutRuleAssetAllocationSchema,
    InRuleAssetAllocationSchema,
    RuleAssetAllocationSchema
)
from app.service.rule_asset_allocation import RuleAssetAllocationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_rule_asset_allocation(
    payload: InRuleAssetAllocationSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save rule asset allocation data. """
    rule_asset_allocation_service = RuleAssetAllocationService(db)
    rule_asset_allocation_service = await rule_asset_allocation_service.create(payload)
    return rule_asset_allocation_service


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_rule_asset_allocation(
    payload:RuleAssetAllocationSchema , db: AsyncSession = Depends(get_db)
):
    """ api to update rule asset allocation  data. """
    rule_asset_allocation_service = RuleAssetAllocationService(db)
    await rule_asset_allocation_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_rule_asset_allocation_by_id(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to fetch all rule asset data. """
    rule_asset_allocation_service = RuleAssetAllocationService(db)
    rule_asset_allocation_service = await rule_asset_allocation_service.get_by_id(uuid)
    return rule_asset_allocation_service


@router.get("/", status_code=status.HTTP_200_OK)
async def get_rule_asset_allocation(db: AsyncSession = Depends(get_db)):
    """ api to fetch all rule asset data. """
    rule_asset_allocation_service = RuleAssetAllocationService(db)
    rule_asset_allocation_service = await rule_asset_allocation_service.get_all()
    return rule_asset_allocation_service


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_rule_asset_allocation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to Fetch data by id. """
    rule_asset_allocation_service = RuleAssetAllocationService(db)
    return await rule_asset_allocation_service.delete(uuid)

