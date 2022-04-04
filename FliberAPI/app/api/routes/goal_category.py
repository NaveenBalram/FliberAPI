import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.goal_category import (
    OutGoalCategorySchema,
    InGoalCategorySchema,
    GoalCategorySchema,
)
from app.service.goal_category import GoalCategoryService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_goal_category(
    payload: InGoalCategorySchema, db: AsyncSession = Depends(get_db)
):
    """ api to save goal category data."""
    goal_category_service = GoalCategoryService(db)
    goal_category = await goal_category_service.create(payload)
    return goal_category


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_goal_category(
    payload: GoalCategorySchema, db: AsyncSession = Depends(get_db)
):
    """ api to update goal category data."""
    goal_category_service = GoalCategoryService(db)
    await goal_category_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK
)
async def get_goal_category(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch goal category data by id."""
    goal_category_service = GoalCategoryService(db)
    goal_category = await goal_category_service.get_by_id(uuid)
    return goal_category


@router.get("/", status_code=status.HTTP_200_OK)
async def get_goal_category(db: AsyncSession = Depends(get_db)):
    """ api to fetch all goal category data by id."""
    goal_category_service = GoalCategoryService(db)
    goal_category = await goal_category_service.get_all()
    return goal_category


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_goal_category(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete goal category data by id."""
    goal_category_service = GoalCategoryService(db)
    await goal_category_service.delete(uuid)

