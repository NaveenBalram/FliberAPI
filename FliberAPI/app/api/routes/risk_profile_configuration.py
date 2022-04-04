import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.risk_profile_configuration import (
    OutRiskProfileConfigurationSchema,
    InRiskProfileConfigurationSchema, RiskProfileConfigurationSchema,
)
from app.service.risk_profile_configuration import RiskProfileConfigurationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=OutRiskProfileConfigurationSchema,
)
async def create_risk_profile_configuration(
    payload: InRiskProfileConfigurationSchema, db: AsyncSession = Depends(get_db)
) -> OutRiskProfileConfigurationSchema:
    """ api to save risk profile configuration data. """
    risk_profile_configuration_service = RiskProfileConfigurationService(db)
    risk_profile_configuration = await risk_profile_configuration_service.create(
        payload
    )
    return risk_profile_configuration


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_risk_profile_configuration(
    payload: RiskProfileConfigurationSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update risk profile configuration data. """
    risk_profile_configuration_service = RiskProfileConfigurationService(db)
    await risk_profile_configuration_service.update(payload)


@router.get(
    "/{uuid}",
    status_code=status.HTTP_200_OK,
    response_model=OutRiskProfileConfigurationSchema,
)
async def get_risk_profile_configuration(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutRiskProfileConfigurationSchema:
    """ api to get risk profile configuration data by id. """
    risk_profile_configuration_service = RiskProfileConfigurationService(db)
    risk_profile_configuration = await risk_profile_configuration_service.get_by_id(
        uuid
    )
    return risk_profile_configuration


@router.get("/", status_code=status.HTTP_200_OK)
async def get_risk_profile_configuration(db: AsyncSession = Depends(get_db)):
    """ api to get risk profile configuration data. """
    risk_profile_configuration_service = RiskProfileConfigurationService(db)
    risk_profile_configuration = await risk_profile_configuration_service.get_all()
    return risk_profile_configuration


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_risk_profile_configuration(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete risk profile configuration data by id. """
    risk_profile_configuration_service = RiskProfileConfigurationService(db)
    await risk_profile_configuration_service.delete(uuid)


