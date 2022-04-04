import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.user_goals import (
    OutUserGoalsSchema,
    UserGoalsSchema,
    UserGoalsSchemaBase,
)
from app.service.user_goals import UserGoalsService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutUserGoalsSchema
)
async def create_user_goals(
    payload: UserGoalsSchemaBase, db: AsyncSession = Depends(get_db)
) -> OutUserGoalsSchema:
    """ api to save user goals data. """
    user_goals_service = UserGoalsService(db)
    user_goals = await user_goals_service.create(payload)
    return user_goals


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_user_goals(
    payload: UserGoalsSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update user goals data. """
    user_goals_service = UserGoalsService(db)
    await user_goals_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutUserGoalsSchema
)
async def get_user_goals(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutUserGoalsSchema:
    """ api to get user goals data by id. """
    user_goals_service = UserGoalsService(db)
    user_goals = await user_goals_service.get_by_id(uuid)
    return user_goals


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user_goals(db: AsyncSession = Depends(get_db)):
    """ api to get all user goals data. """
    user_goals_service = UserGoalsService(db)
    user_goals = await user_goals_service.get_all()
    return user_goals


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_user_goals(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete user goals data by id. """
    user_goals_service = UserGoalsService(db)
    await user_goals_service.delete(uuid)


@router.get("/by/user/id/{uuid}", status_code=status.HTTP_200_OK)
async def get_user_goals_by_user(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """api to get the user goals data using user id."""

    user_goals_service = UserGoalsService(db)
    return await user_goals_service.get_by_user_id(user_id)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_user_goals_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete user goals data user id. """
    user_goals_service = UserGoalsService(db)
    await user_goals_service.delete(user_id)
