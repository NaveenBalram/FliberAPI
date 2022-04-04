import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.rate import OutRateSchema, InRateSchema, RateSchema
from app.service.rate import RateService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OutRateSchema)
async def create_rate(
    payload: InRateSchema, db: AsyncSession = Depends(get_db)
) -> OutRateSchema:
    """ api to save rate data. """
    rate_service = RateService(db)
    rate = await rate_service.create(payload)
    return rate


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_rate(payload: RateSchema, db: AsyncSession = Depends(get_db)):
    """ api to update rate data. """
    rate_service = RateService(db)
    await rate_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=OutRateSchema)
async def get_rate(uuid: UUID, db: AsyncSession = Depends(get_db)) -> OutRateSchema:
    """ api to get rate data by id. """
    rate_service = RateService(db)
    rate = await rate_service.get_by_id(uuid)
    return rate


@router.get("/", status_code=status.HTTP_200_OK)
async def get_rate(db: AsyncSession = Depends(get_db)):
    """ api to get rate data. """
    rate_service = RateService(db)
    rate = await rate_service.get_all()
    return rate


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_rate(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete rate data by id. """
    rate_service = RateService(db)
    await rate_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_rate_by_user_id(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete rate data by user_id. """
    rate_service = RateService(db)
    await rate_service.delete(user_id)
