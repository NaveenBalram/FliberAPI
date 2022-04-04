import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.bse_account_type import (
    OutBseAccountTypeSchema,
    InBseAccountTypeSchema,
    BseAccountTypeSchema,
)
from app.service.bse_account_type import BseAccountTypeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_bse_account_type(
    payload: InBseAccountTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save bse account type data. """
    bse_account_type_service = BseAccountTypeService(db)
    bse_account_type = await bse_account_type_service.create(payload)
    return bse_account_type


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_bse_account_type(
    payload: BseAccountTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update bse account type data. """
    bse_account_type_service = BseAccountTypeService(db)
    await bse_account_type_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutBseAccountTypeSchema
)
async def get_bse_account_type(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch bse account type data by id. """
    bse_account_type_service = BseAccountTypeService(db)
    bse_account_type = await bse_account_type_service.get_by_id(uuid)
    return bse_account_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_bse_account_type(db: AsyncSession = Depends(get_db)):
    """ api to fetch all bse account type data. """
    bse_account_type_service = BseAccountTypeService(db)
    bse_account_type = await bse_account_type_service.get_all()
    return bse_account_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_bse_account_type(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete bse account type data by id. """
    bse_account_type_service = BseAccountTypeService(db)
    return await bse_account_type_service.delete(uuid)


