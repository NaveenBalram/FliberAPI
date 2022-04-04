import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.funds_type import (
    OutFundsTypeSchema,
    InFundsTypeSchema,
    FundsTypeSchema,
)
from app.service.funds_type import FundsTypeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_funds_type(
    payload: InFundsTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save funds type data. """
    funds_type_service = FundsTypeService(db)
    funds_type = await funds_type_service.create(payload)
    return funds_type


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_funds_type(
    payload: FundsTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update funds type data. """
    funds_type_service = FundsTypeService(db)
    await funds_type_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK
)
async def get_funds_type(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch funds type data by id. """
    funds_type_service = FundsTypeService(db)
    funds_type = await funds_type_service.get_by_id(uuid)
    return funds_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_funds_type(db: AsyncSession = Depends(get_db)):
    """ api to fetch all funds type data. """
    funds_type_service = FundsTypeService(db)
    funds_type = await funds_type_service.get_all()
    return funds_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_funds_type(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete funds type data by id. """
    funds_type_service = FundsTypeService(db)
    return await funds_type_service.delete(uuid)

