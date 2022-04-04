import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.goal_type import (
    InGoalTypeSchema,
    GoalTypeSchema,
)
from app.service.goal_type import GoalTypeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_goal_type(
        payload: InGoalTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save goal type data."""
    goal_type_service = GoalTypeService(db)
    goal_type = await goal_type_service.create(payload)
    return goal_type


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_goal_type(payload: GoalTypeSchema, db: AsyncSession = Depends(get_db)):
    """ api to update goal type data."""
    goal_type_service = GoalTypeService(db)
    await goal_type_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_goal_type(
        uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to save goal type data by id."""
    goal_type_service = GoalTypeService(db)
    goal_type = await goal_type_service.get_by_id(uuid)
    return goal_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_goal_type(db: AsyncSession = Depends(get_db)):
    """ api to fetch all goal type data. """
    goal_type_service = GoalTypeService(db)
    goal_type = await goal_type_service.get_all()
    return goal_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_goal_type(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete goal type data by id."""
    goal_type_service = GoalTypeService(db)
    await goal_type_service.delete(uuid)

