import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.income_type import (
    InIncomeTypeSchema,
    IncomeTypeSchema,
)
from app.service.income_type import IncomeTypeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED,
)
async def create_income_type(
        payload: InIncomeTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save income type data."""
    income_type_service = IncomeTypeService(db)
    income_type = await income_type_service.create(payload)
    return income_type


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_income_type(
        payload: IncomeTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update income category data."""
    income_type_service = IncomeTypeService(db)
    await income_type_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK
)
async def get_income_type(
        uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to get income category data by id."""
    income_type_service = IncomeTypeService(db)
    income_type = await income_type_service.get_by_id(uuid)
    return income_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_income_type(db: AsyncSession = Depends(get_db)):
    """ api to fetch all income category data."""
    income_type_service = IncomeTypeService(db)
    income_type = await income_type_service.get_all()
    return income_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_income_type(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete income category data by id."""
    income_type_service = IncomeTypeService(db)
    await income_type_service.delete(uuid)

