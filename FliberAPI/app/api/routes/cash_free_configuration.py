import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.cash_free_configuration import (
    OutCashFreeConfigurationSchema,
    InCashFreeConfigurationSchema,
    CashFreeConfigurationSchemaBase,
    CashFreeConfigurationSchema,
)
from app.service.cash_free_configuration import CashFreeConfigurationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_cash_free_configuration(
    payload: InCashFreeConfigurationSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save cash free configuration. """
    cash_free_configuration_service = CashFreeConfigurationService(db)
    cash_free_configuration = await cash_free_configuration_service.create(payload)
    return cash_free_configuration


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_cash_free_configuration(
    payload: CashFreeConfigurationSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update cash free configuration. """
    cash_free_configuration_service = CashFreeConfigurationService(db)
    await cash_free_configuration_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_cash_free_configuration(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to fetch cash free configuration by id """
    cash_free_configuration_service = CashFreeConfigurationService(db)
    cash_free_configuration = await cash_free_configuration_service.get_by_id(uuid)
    return cash_free_configuration


@router.get("/", status_code=status.HTTP_200_OK)
async def get_cash_free_configuration(db: AsyncSession = Depends(get_db)):
    """ api to fetch all  cash free configuration data """
    cash_free_configuration_service = CashFreeConfigurationService(db)
    cash_free_configuration = await cash_free_configuration_service.get_all()
    return cash_free_configuration


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_cash_free_configuration(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete cash free configuration data"""
    cash_free_configuration_service = CashFreeConfigurationService(db)
    await cash_free_configuration_service.delete(uuid)
