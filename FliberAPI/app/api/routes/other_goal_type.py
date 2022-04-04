import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.other_goal_type import (
    OutOtherGoalTypeSchema,
    InOtherGoalTypeSchema,
    OtherGoalTypeSchema,
)
from app.service.other_goal_type import OtherGoalTypeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutOtherGoalTypeSchema
)
async def create_other_goal_type(
    payload: InOtherGoalTypeSchema, db: AsyncSession = Depends(get_db)
) -> OutOtherGoalTypeSchema:
    """ api to save other goal type data. """
    other_goal_type_service = OtherGoalTypeService(db)
    other_goal_type = await other_goal_type_service.create(payload)
    return other_goal_type


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_other_goal_type(
    payload: OtherGoalTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update other goal type data. """
    other_goal_type_service = OtherGoalTypeService(db)
    await other_goal_type_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutOtherGoalTypeSchema
)
async def get_other_goal_type(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutOtherGoalTypeSchema:
    """ api to get other goal type data by id. """
    other_goal_type_service = OtherGoalTypeService(db)
    other_goal_type = await other_goal_type_service.get_by_id(uuid)
    return other_goal_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_other_goal_type(db: AsyncSession = Depends(get_db)):
    """ api to get other goal type data. """
    other_goal_type_service = OtherGoalTypeService(db)
    other_goal_type = await other_goal_type_service.get_all()
    return other_goal_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_other_goal_type(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete other goal type data by id. """
    other_goal_type_service = OtherGoalTypeService(db)
    await other_goal_type_service.delete(uuid)


# @router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
# async def delete_other_goal_type_by_user_id(
#     user_id: UUID, db: AsyncSession = Depends(get_db)
# ):
#     """ api to  other goal type data. """
#     other_goal_type_service = OtherGoalTypeService(db)
#     await other_goal_type_service.delete(user_id)
