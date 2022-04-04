import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.user_answers import (
    OutUserAnswersSchema,
    InUserAnswersSchema,
    UserAnswersSchema,
)
from app.service.user_answers import UserAnswersService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutUserAnswersSchema
)
async def create_user_answers(
    payload: InUserAnswersSchema, db: AsyncSession = Depends(get_db)
) -> OutUserAnswersSchema:
    """ api to save user answers data. """
    user_answers_service = UserAnswersService(db)
    user_answers = await user_answers_service.create(payload)
    return user_answers


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_user_answers(
    payload: UserAnswersSchema, db: AsyncSession = Depends(get_db)
):
    """ api to  user answers data. """
    user_answers_service = UserAnswersService(db)
    await user_answers_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutUserAnswersSchema
)
async def get_user_answers(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutUserAnswersSchema:
    """ api to  user answers data. """
    user_answers_service = UserAnswersService(db)
    user_answers = await user_answers_service.get_by_id(uuid)
    return user_answers


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user_answers(db: AsyncSession = Depends(get_db)):
    """ api to get user answers data. """
    user_answers_service = UserAnswersService(db)
    user_answers = await user_answers_service.get_all()
    return user_answers


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_user_answers(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete user answers data by id. """
    user_answers_service = UserAnswersService(db)
    await user_answers_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_user_answers_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to  user answers data. """
    user_answers_service = UserAnswersService(db)
    await user_answers_service.delete(user_id)
