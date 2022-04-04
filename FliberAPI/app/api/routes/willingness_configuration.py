import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.willingness_configuration import (
    OutWillingnessConfigurationSchema,
    InWillingnessConfigurationSchema, WillingnessConfigurationSchema,
)
from app.service.willingness_configuration import WillingnessConfigurationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
async def create_willingness_configuration(
    payload: InWillingnessConfigurationSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save willingness configuration data. """
    willingness_configuration_service = WillingnessConfigurationService(db)
    willingness_configuration = await willingness_configuration_service.create(payload)
    return willingness_configuration


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_willingness_configuration(
    payload: WillingnessConfigurationSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update willingness configuration data. """
    willingness_configuration_service = WillingnessConfigurationService(db)
    await willingness_configuration_service.update(payload)


@router.get(
    "/{uuid}",
    status_code=status.HTTP_200_OK,
    response_model=OutWillingnessConfigurationSchema,
)
async def get_willingness_configuration(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutWillingnessConfigurationSchema:
    """ api to get willingness configuration data by id. """
    willingness_configuration_service = WillingnessConfigurationService(db)
    willingness_configuration = await willingness_configuration_service.get_by_id(uuid)
    return willingness_configuration


@router.get("/", status_code=status.HTTP_200_OK)
async def get_willingness_configuration(db: AsyncSession = Depends(get_db)):
    """ api to get willingness configuration data. """
    willingness_configuration_service = WillingnessConfigurationService(db)
    willingness_configuration = await willingness_configuration_service.get_all()
    return willingness_configuration


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_willingness_configuration(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete willingness configuration data by id. """
    willingness_configuration_service = WillingnessConfigurationService(db)
    await willingness_configuration_service.delete(uuid)



