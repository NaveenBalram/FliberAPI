import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.submit_question import (
    OutSubmitQuestionSchema,
    InSubmitQuestionSchema,
    SubmitQuestionSchema,
    SubmitQuestionSchemaBase,
)
from app.service.submit_question import SubmitQuestionService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutSubmitQuestionSchema
)
async def create_submit_question(
    payload: InSubmitQuestionSchema, db: AsyncSession = Depends(get_db)
) -> OutSubmitQuestionSchema:
    """ api to save submit question data. """
    submit_question_service = SubmitQuestionService(db)
    submit_question = await submit_question_service.create(payload)
    return submit_question


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_submit_question(
    payload: SubmitQuestionSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update submit question data. """
    submit_question_service = SubmitQuestionService(db)
    await submit_question_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutSubmitQuestionSchema
)
async def get_submit_question(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutSubmitQuestionSchema:
    """ api to get submit question data by id. """
    submit_question_service = SubmitQuestionService(db)
    submit_question = await submit_question_service.get_by_id(uuid)
    return submit_question


@router.get("/", status_code=status.HTTP_200_OK)
async def get_submit_question(db: AsyncSession = Depends(get_db)):
    """ api to get submit question data. """
    submit_question_service = SubmitQuestionService(db)
    submit_question = await submit_question_service.get_all()
    return submit_question


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_submit_question(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete submit question data by id. """
    submit_question_service = SubmitQuestionService(db)
    await submit_question_service.delete(uuid)


@router.post("/bulk/create", status_code=status.HTTP_201_CREATED)
async def create_submit_question(
    payload: list[SubmitQuestionSchemaBase], db: AsyncSession = Depends(get_db)
):
    """ api to bulk save submit question data. """
    submit_question_service = SubmitQuestionService(db)
    submit_question = await submit_question_service.bulk_create(payload)
    return submit_question


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_submit_question_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete submit question data user id. """
    submit_question_service = SubmitQuestionService(db)
    await submit_question_service.delete(user_id)
