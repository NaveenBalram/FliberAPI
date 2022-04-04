import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.question import (
    OutQuestionSchema,
    InQuestionSchema,
    QuestionSchema,
)
from app.service.question import QuestionService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OutQuestionSchema)
async def create_question(
    payload: InQuestionSchema, db: AsyncSession = Depends(get_db)
) -> OutQuestionSchema:
    """ api to save question data. """
    question_service = QuestionService(db)
    question = await question_service.create(payload)
    return question


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_question(payload: QuestionSchema, db: AsyncSession = Depends(get_db)):
    """ api to update question data. """
    question_service = QuestionService(db)
    await question_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=OutQuestionSchema)
async def get_question(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutQuestionSchema:
    """ api to get question data by id. """
    question_service = QuestionService(db)
    question = await question_service.get_by_id(uuid)
    return question


@router.get("/", status_code=status.HTTP_200_OK)
async def get_question(db: AsyncSession = Depends(get_db)):
    """ api to get question data. """
    question_service = QuestionService(db)
    question = await question_service.get_all()
    return question


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_question(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete question data by id. """
    question_service = QuestionService(db)
    await question_service.delete(uuid)


#
# @router.get("/get/by/module/type", status_code=status.HTTP_200_OK)
# async def get_question(module_type: int, db: AsyncSession = Depends(get_db)):
#     """ api to get question data. """
#     question_service = QuestionService(db)
#     question = await question_service.question_info(module_type)
#     return question


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_question_by_user_id(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete question data by user_id. """
    question_service = QuestionService(db)
    await question_service.delete(user_id)
