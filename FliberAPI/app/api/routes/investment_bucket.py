import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.investment_bucket import (
    OutInvestmentBucketSchema,
    InInvestmentBucketSchema,
    InvestmentBucketSchema,
)
from app.service.investment_bucket import InvestmentBucketService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutInvestmentBucketSchema
)
async def create_investment_bucket(
    payload: InInvestmentBucketSchema, db: AsyncSession = Depends(get_db)
) -> OutInvestmentBucketSchema:
    """ api to  investment bucket data. """
    investment_bucket_service = InvestmentBucketService(db)
    investment_bucket = await investment_bucket_service.create(payload)
    return investment_bucket


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_investment_bucket(
    payload: InvestmentBucketSchema, db: AsyncSession = Depends(get_db)
):
    """ api to  investment bucket data. """
    investment_bucket_service = InvestmentBucketService(db)
    await investment_bucket_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutInvestmentBucketSchema
)
async def get_investment_bucket(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutInvestmentBucketSchema:
    """ api to  investment bucket data. """
    investment_bucket_service = InvestmentBucketService(db)
    investment_bucket = await investment_bucket_service.get_by_id(uuid)
    return investment_bucket


@router.get("/", status_code=status.HTTP_200_OK)
async def get_investment_bucket(db: AsyncSession = Depends(get_db)):
    """ api to get investment bucket data. """
    investment_bucket_service = InvestmentBucketService(db)
    investment_bucket = await investment_bucket_service.get_all()
    return investment_bucket


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_investment_bucket(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete investment bucket data by id. """
    investment_bucket_service = InvestmentBucketService(db)
    await investment_bucket_service.delete(uuid)

