import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.rr_score_configuration import (
    OutRrScoreConfigurationSchema,
    InRrScoreConfigurationSchema, RrScoreConfigurationSchema,
)
from app.service.rr_score_configuration import RrScoreConfigurationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=OutRrScoreConfigurationSchema,
)
async def create_rr_score_configuration(
    payload: InRrScoreConfigurationSchema, db: AsyncSession = Depends(get_db)
) -> OutRrScoreConfigurationSchema:
    """ api to save rr score configuration data. """
    rr_score_configuration_service = RrScoreConfigurationService(db)
    rr_score_configuration = await rr_score_configuration_service.create(payload)
    return rr_score_configuration


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_rr_score_configuration(
    payload: RrScoreConfigurationSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update rr score configuration data. """
    rr_score_configuration_service = RrScoreConfigurationService(db)
    await rr_score_configuration_service.update(payload)


@router.get(
    "/{uuid}",
    status_code=status.HTTP_200_OK,
    response_model=OutRrScoreConfigurationSchema,
)
async def get_rr_score_configuration(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutRrScoreConfigurationSchema:
    """ api to get rr score configuration data by id. """
    rr_score_configuration_service = RrScoreConfigurationService(db)
    rr_score_configuration = await rr_score_configuration_service.get_by_id(uuid)
    return rr_score_configuration


@router.get("/", status_code=status.HTTP_200_OK)
async def get_rr_score_configuration(db: AsyncSession = Depends(get_db)):
    """ api to get rr score configuration data. """
    rr_score_configuration_service = RrScoreConfigurationService(db)
    rr_score_configuration = await rr_score_configuration_service.get_all()
    return rr_score_configuration


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_rr_score_configuration(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete rr score configuration data by id. """
    rr_score_configuration_service = RrScoreConfigurationService(db)
    await rr_score_configuration_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_rr_score_configuration_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete rr score configuration data user id. """
    rr_score_configuration_service = RrScoreConfigurationService(db)
    await rr_score_configuration_service.delete(user_id)
