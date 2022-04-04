import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.pre_retirement_configuration import (
    OutPreRetirementConfigurationSchema,
    InPreRetirementConfigurationSchema,
    PreRetirementConfigurationSchema,
)
from app.service.pre_retirement_configuration import PreRetirementConfigurationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=OutPreRetirementConfigurationSchema,
)
async def create_pre_retirement_configuration(
    payload: InPreRetirementConfigurationSchema, db: AsyncSession = Depends(get_db)
) -> OutPreRetirementConfigurationSchema:
    """ api to save pre retirement configuration data. """
    pre_retirement_configuration_service = PreRetirementConfigurationService(db)
    pre_retirement_configuration = await pre_retirement_configuration_service.create(
        payload
    )
    return pre_retirement_configuration


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_pre_retirement_configuration(
    payload: PreRetirementConfigurationSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update pre retirement configuration data. """
    pre_retirement_configuration_service = PreRetirementConfigurationService(db)
    await pre_retirement_configuration_service.update(payload)


@router.get(
    "/{uuid}",
    status_code=status.HTTP_200_OK,
    response_model=OutPreRetirementConfigurationSchema,
)
async def get_pre_retirement_configuration(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutPreRetirementConfigurationSchema:
    """ api to get pre retirement configuration data by id. """
    pre_retirement_configuration_service = PreRetirementConfigurationService(db)
    pre_retirement_configuration = await pre_retirement_configuration_service.get_by_id(
        uuid
    )
    return pre_retirement_configuration


@router.get("/", status_code=status.HTTP_200_OK)
async def get_pre_retirement_configuration(db: AsyncSession = Depends(get_db)):
    """ api to get pre retirement configuration data. """
    pre_retirement_configuration_service = PreRetirementConfigurationService(db)
    pre_retirement_configuration = await pre_retirement_configuration_service.get_all()
    return pre_retirement_configuration


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_pre_retirement_configuration(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete  pre retirement configuration data by id. """
    pre_retirement_configuration_service = PreRetirementConfigurationService(db)
    await pre_retirement_configuration_service.delete(uuid)


