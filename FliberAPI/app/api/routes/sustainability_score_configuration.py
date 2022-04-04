import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.sustainability_score_configuration import (
    OutSustainabilityScoreConfigurationSchema,
    InSustainabilityScoreConfigurationSchema, SustainabilityScoreConfigurationSchema,
)
from app.service.sustainability_score_configuration import (
    SustainabilityScoreConfigurationService,
)

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=OutSustainabilityScoreConfigurationSchema,
)
async def create_sustainability_score_configuration(
    payload: InSustainabilityScoreConfigurationSchema,
    db: AsyncSession = Depends(get_db),
) -> OutSustainabilityScoreConfigurationSchema:
    """ api to save sustainability score configuration data. """
    sustainability_score_configuration_service = (
        SustainabilityScoreConfigurationService(db)
    )
    sustainability_score_configuration = (
        await sustainability_score_configuration_service.create(payload)
    )
    return sustainability_score_configuration


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_sustainability_score_configuration(
    payload: SustainabilityScoreConfigurationSchema,
    db: AsyncSession = Depends(get_db),
):
    """ api to update sustainability score configuration data. """
    sustainability_score_configuration_service = (
        SustainabilityScoreConfigurationService(db)
    )
    await sustainability_score_configuration_service.update(payload)


@router.get(
    "/{uuid}",
    status_code=status.HTTP_200_OK,
    response_model=OutSustainabilityScoreConfigurationSchema,
)
async def get_sustainability_score_configuration(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutSustainabilityScoreConfigurationSchema:
    """ api to get sustainability score configuration data by id. """
    sustainability_score_configuration_service = (
        SustainabilityScoreConfigurationService(db)
    )
    sustainability_score_configuration = (
        await sustainability_score_configuration_service.get_by_id(uuid)
    )
    return sustainability_score_configuration


@router.get("/", status_code=status.HTTP_200_OK)
async def get_sustainability_score_configuration(db: AsyncSession = Depends(get_db)):
    """ api to get sustainability score configuration data. """
    sustainability_score_configuration_service = (
        SustainabilityScoreConfigurationService(db)
    )
    sustainability_score_configuration = (
        await sustainability_score_configuration_service.get_all()
    )
    return sustainability_score_configuration


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_sustainability_score_configuration(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete sustainability score configuration data by id. """
    sustainability_score_configuration_service = (
        SustainabilityScoreConfigurationService(db)
    )
    await sustainability_score_configuration_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_sustainability_score_configuration_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete sustainability score configuration data by user id. """
    sustainability_score_configuration_service = (
        SustainabilityScoreConfigurationService(db)
    )
    await sustainability_score_configuration_service.delete(user_id)
