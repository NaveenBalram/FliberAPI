import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.funds_category import (
    InFundsCategorySchema,
    FundsCategorySchema,
)
from app.service.funds_category import FundsCategoryService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_funds_category(payload: InFundsCategorySchema, db: AsyncSession = Depends(get_db)):
    """ api to save fund category data. """
    funds_category_service = FundsCategoryService(db)
    funds_category = await funds_category_service.create(payload)
    return funds_category


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_funds_category(payload: FundsCategorySchema, db: AsyncSession = Depends(get_db)):
    """ api to update fund category data. """
    funds_category_service = FundsCategoryService(db)
    await funds_category_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_funds_category(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to fetch all fund category data. """
    funds_category_service = FundsCategoryService(db)
    funds_category = await funds_category_service.get_by_id(uuid)
    return funds_category


@router.get("/", status_code=status.HTTP_200_OK)
async def get_funds_category(db: AsyncSession = Depends(get_db)):
    """ api to fetch all fund category data. """
    funds_category_service = FundsCategoryService(db)
    funds_category = await funds_category_service.get_all()
    return funds_category


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_funds_category(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete fund category data by id. """
    funds_category_service = FundsCategoryService(db)
    return await funds_category_service.delete(uuid)
