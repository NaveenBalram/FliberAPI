import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.instrument_type import (
    OutInstrumentTypeSchema,
    InInstrumentTypeSchema,
    InstrumentTypeSchema,
)
from app.service.instrument_type import InstrumentTypeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutInstrumentTypeSchema
)
async def create_instrument_type(
    payload: InInstrumentTypeSchema, db: AsyncSession = Depends(get_db)
) -> OutInstrumentTypeSchema:
    instrument_type_service = InstrumentTypeService(db)
    instrument_type = await instrument_type_service.create(payload)
    return instrument_type


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_instrument_type(
    payload: InstrumentTypeSchema, db: AsyncSession = Depends(get_db)
):
    instrument_type_service = InstrumentTypeService(db)
    await instrument_type_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutInstrumentTypeSchema
)
async def get_instrument_type(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutInstrumentTypeSchema:
    instrument_type_service = InstrumentTypeService(db)
    instrument_type = await instrument_type_service.get_by_id(uuid)
    return instrument_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_instrument_type(db: AsyncSession = Depends(get_db)):
    instrument_type_service = InstrumentTypeService(db)
    instrument_type = await instrument_type_service.get_all()
    return instrument_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_instrument_type(uuid: UUID, db: AsyncSession = Depends(get_db)):
    instrument_type_service = InstrumentTypeService(db)
    await instrument_type_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_instrument_type_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    instrument_type_service = InstrumentTypeService(db)
    await instrument_type_service.delete(user_id)
