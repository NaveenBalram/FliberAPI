import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.income_category import (
    OutIncomeCategorySchema,
    InIncomeCategorySchema,
    IncomeCategorySchema,
)
from app.service.income_category import IncomeCategoryService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED,
)
async def create_income_category(
    payload: InIncomeCategorySchema, db: AsyncSession = Depends(get_db)
):
    """ api to save income category data."""
    income_category_service = IncomeCategoryService(db)
    income_category = await income_category_service.create(payload)
    return income_category


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_income_category(
    payload: IncomeCategorySchema, db: AsyncSession = Depends(get_db)
):
    """ api to save income category data."""
    income_category_service = IncomeCategoryService(db)
    await income_category_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK
)
async def get_income_category(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch income category data by id."""
    income_category_service = IncomeCategoryService(db)
    income_category = await income_category_service.get_by_id(uuid)
    return income_category


@router.get("/", status_code=status.HTTP_200_OK)
async def get_income_category(db: AsyncSession = Depends(get_db)):
    """ api to get all income category data."""
    income_category_service = IncomeCategoryService(db)
    income_category = await income_category_service.get_all()
    return income_category


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_income_category(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete income category data by id."""
    income_category_service = IncomeCategoryService(db)
    await income_category_service.delete(uuid)

