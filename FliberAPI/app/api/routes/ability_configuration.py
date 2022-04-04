import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.ability_configuration import (
    InAbilityConfigurationSchema,
    AbilityConfigurationSchema,
)
from app.service.ability_configuration import AbilityConfigurationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_ability_configuration(
    payload: InAbilityConfigurationSchema, db: AsyncSession = Depends(get_db)
):
    """Api to save ability configurations to database."""
    try:
        ability_configuration_service = AbilityConfigurationService(db)
        ability_configuration = await ability_configuration_service.create(payload)
        return ability_configuration
    except Exception as e:
        return {"error": str(e)}


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_ability_configuration(
    payload: AbilityConfigurationSchema, db: AsyncSession = Depends(get_db)
):
    """Api to update ability configurations to table."""
    try:
        ability_configuration_service = AbilityConfigurationService(db)
        await ability_configuration_service.update(payload)
    except Exception as e:
        return {"error": str(e)}


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_ability_configuration(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """Api to fetch ability configurations by user id."""
    try:
        ability_configuration_service = AbilityConfigurationService(db)
        ability_configuration = await ability_configuration_service.get_by_id(uuid)
        return ability_configuration
    except Exception as e:
        return {"error": str(e)}


@router.get("/", status_code=status.HTTP_200_OK)
async def get_ability_configuration(db: AsyncSession = Depends(get_db)):
    """Api to fetch all ability configurations from table."""
    try:
        ability_configuration_service = AbilityConfigurationService(db)
        ability_configuration = await ability_configuration_service.get_all()
        return ability_configuration
    except Exception as e:
        return {"error": str(e)}


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_ability_configuration(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """Api to delete ability configurations by id."""
    try:
        ability_configuration_service = AbilityConfigurationService(db)
        return await ability_configuration_service.delete(uuid)
    except Exception as e:
        return {"error": str(e)}


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_ability_configuration_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """Api to delete ability configurations using user id."""
    try:
        ability_configuration_service = AbilityConfigurationService(db)
        return await ability_configuration_service.delete(user_id)
    except Exception as e:
        return {"error": str(e)}
