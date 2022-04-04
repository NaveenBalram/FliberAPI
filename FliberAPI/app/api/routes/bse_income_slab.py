import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.bse_income_slab import (
    OutBSEIncomeSlabSchema,
    InBSEIncomeSlabSchema,
    BSEIncomeSlabSchema,
)
from app.service.bse_income_slab import BSEIncomeSlabService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_bse_income_slab(
    payload: InBSEIncomeSlabSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save bse income slab data. """
    bse_income_slab_service = BSEIncomeSlabService(db)
    bse_income_slab = await bse_income_slab_service.create(payload)
    return bse_income_slab


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_bse_income_slab(
    payload: BSEIncomeSlabSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update bse income slab data. """
    bse_income_slab_service = BSEIncomeSlabService(db)
    await bse_income_slab_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK
)
async def get_bse_income_slab(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch bse income slab data by id. """
    bse_income_slab_service = BSEIncomeSlabService(db)
    bse_income_slab = await bse_income_slab_service.get_by_id(uuid)
    return bse_income_slab


@router.get("/", status_code=status.HTTP_200_OK)
async def get_bse_income_slab(db: AsyncSession = Depends(get_db)):
    """ api to fetch all bse income slab data. """
    bse_income_slab_service = BSEIncomeSlabService(db)
    bse_income_slab = await bse_income_slab_service.get_all()
    return bse_income_slab


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_bse_income_slab(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete bse income slab data by id. """
    bse_income_slab_service = BSEIncomeSlabService(db)
    return await bse_income_slab_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_bse_income_slab_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete bse income slab data by user id. """
    bse_income_slab_service = BSEIncomeSlabService(db)
    return await bse_income_slab_service.delete(user_id)
