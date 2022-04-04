import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.frequency import (
    OutFrequencySchema,
    InFrequencySchema,
    FrequencySchema,
)
from app.service.frequency import FrequencyService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_frequency(
    payload: InFrequencySchema, db: AsyncSession = Depends(get_db)
):
    """ api to save frequency data. """
    frequency_service = FrequencyService(db)
    frequency = await frequency_service.create(payload)
    return frequency


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_frequency(
    payload: FrequencySchema, db: AsyncSession = Depends(get_db)
):
    """ api to update frequency data. """
    frequency_service = FrequencyService(db)
    await frequency_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK
)
async def get_frequency(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch frequency data by id. """
    frequency_service = FrequencyService(db)
    frequency = await frequency_service.get_by_id(uuid)
    return frequency


@router.get("/", status_code=status.HTTP_200_OK)
async def get_frequency(db: AsyncSession = Depends(get_db)):
    """ api to fetch all frequency data. """
    frequency_service = FrequencyService(db)
    frequency = await frequency_service.get_all()
    return frequency


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_frequency(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete frequency data by id. """
    frequency_service = FrequencyService(db)
    return await frequency_service.delete(uuid)


# @router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
# async def delete_frequency_by_user_id(
#     user_id: UUID, db: AsyncSession = Depends(get_db)
# ):
#     """ api to update frequency data. """
#     frequency_service = FrequencyService(db)
#     return await frequency_service.delete(user_id)
