import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.goal_bucket import (
    OutGoalBucketSchema,
    InGoalBucketSchema,
    GoalBucketSchema,
)
from app.service.goal_bucket import GoalBucketService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_goal_bucket(
    payload: InGoalBucketSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save goal bucket data."""
    goal_bucket_service = GoalBucketService(db)
    goal_bucket = await goal_bucket_service.create(payload)
    return goal_bucket


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_goal_bucket(
    payload: GoalBucketSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update goal bucket data."""
    goal_bucket_service = GoalBucketService(db)
    await goal_bucket_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK,
)
async def get_goal_bucket(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch goal bucket data by id."""
    goal_bucket_service = GoalBucketService(db)
    goal_bucket = await goal_bucket_service.get_by_id(uuid)
    return goal_bucket


@router.get("/", status_code=status.HTTP_200_OK)
async def get_goal_bucket(db: AsyncSession = Depends(get_db)):
    """ api to fetch all goal bucket data."""
    goal_bucket_service = GoalBucketService(db)
    goal_bucket = await goal_bucket_service.get_all()
    return goal_bucket


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_goal_bucket(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to save goal bucket data."""
    goal_bucket_service = GoalBucketService(db)
    await goal_bucket_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_goal_bucket_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete goal bucket data."""
    goal_bucket_service = GoalBucketService(db)
    await goal_bucket_service.delete(user_id)
