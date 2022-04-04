import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.phone_api import (
    OutPhoneApiSchema,
    InPhoneApiSchema,
    PhoneApiSchemaBase,
    PhoneApiSchema,
)
from app.service.phone_api import PhoneApiService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_phone_api(
    payload: InPhoneApiSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save phone api data. """
    phone_api_service = PhoneApiService(db)
    phone_api = await phone_api_service.create(payload)
    return phone_api


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_phone_api(payload: PhoneApiSchema, db: AsyncSession = Depends(get_db)):
    """ api to update phone api data. """
    phone_api_service = PhoneApiService(db)
    await phone_api_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_phone_api(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to get phone api data by id. """
    phone_api_service = PhoneApiService(db)
    phone_api = await phone_api_service.get_by_id(uuid)
    return phone_api


@router.get("/", status_code=status.HTTP_200_OK)
async def get_phone_api(db: AsyncSession = Depends(get_db)):
    """ api to get phone api data. """
    phone_api_service = PhoneApiService(db)
    phone_api = await phone_api_service.get_all()
    return phone_api


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_phone_api(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete phone api data by id. """
    phone_api_service = PhoneApiService(db)
    await phone_api_service.delete(uuid)
