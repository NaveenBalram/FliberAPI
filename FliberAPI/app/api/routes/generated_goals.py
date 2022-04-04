import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.generated_goals import (
    InGeneratedGoalsSchema,
    GeneratedGoalsSchema,
)
from app.service.generated_goals import GeneratedGoalsService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_generated_goals(
        payload: InGeneratedGoalsSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save generated goals data. """
    generated_goals_service = GeneratedGoalsService(db)
    generated_goals = await generated_goals_service.create(payload)
    return generated_goals


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_generated_goals(
        payload: GeneratedGoalsSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update generated goals data. """
    generated_goals_service = GeneratedGoalsService(db)
    await generated_goals_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK
)
async def get_generated_goals(
        uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch generated goals data by id."""
    generated_goals_service = GeneratedGoalsService(db)
    generated_goals = await generated_goals_service.get_by_id(uuid)
    return generated_goals


@router.get("/", status_code=status.HTTP_200_OK)
async def get_generated_goals(db: AsyncSession = Depends(get_db)):
    """ api to save generated goals data."""
    generated_goals_service = GeneratedGoalsService(db)
    generated_goals = await generated_goals_service.get_all()
    return generated_goals


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_generated_goals(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete generated goals data by id."""
    generated_goals_service = GeneratedGoalsService(db)
    await generated_goals_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_generated_goals_by_user_id(
        user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete generated goals data by user id."""
    generated_goals_service = GeneratedGoalsService(db)
    await generated_goals_service.delete(user_id)
