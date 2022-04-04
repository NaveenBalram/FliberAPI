import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.post_goal import (
    OutPostGoalSchema,
    InPostGoalSchema,
    PostGoalSchema,
)
from app.service.post_goal import PostGoalService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OutPostGoalSchema)
async def create_post_goal(
    payload: InPostGoalSchema, db: AsyncSession = Depends(get_db)
) -> OutPostGoalSchema:
    """ api to save post goal data. """
    post_goal_service = PostGoalService(db)
    post_goal = await post_goal_service.create(payload)
    return post_goal


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_post_goal(payload: PostGoalSchema, db: AsyncSession = Depends(get_db)):
    """ api to update post goal data. """
    post_goal_service = PostGoalService(db)
    await post_goal_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=OutPostGoalSchema)
async def get_post_goal(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutPostGoalSchema:
    """ api to get post goal data by id. """
    post_goal_service = PostGoalService(db)
    post_goal = await post_goal_service.get_by_id(uuid)
    return post_goal


@router.get("/", status_code=status.HTTP_200_OK)
async def get_post_goal(db: AsyncSession = Depends(get_db)):
    """ api to get post goal data. """
    post_goal_service = PostGoalService(db)
    post_goal = await post_goal_service.get_all()
    return post_goal


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_post_goal(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete post goal data by id. """
    post_goal_service = PostGoalService(db)
    await post_goal_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_post_goal_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete post goal data. """
    post_goal_service = PostGoalService(db)
    await post_goal_service.delete(user_id)
