import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.question_type import (
    OutQuestionTypeSchema,
    InQuestionTypeSchema,
    QuestionTypeSchema,
)
from app.service.question_type import QuestionTypeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutQuestionTypeSchema
)
async def create_question_type(
    payload: InQuestionTypeSchema, db: AsyncSession = Depends(get_db)
) -> OutQuestionTypeSchema:
    """ api to save question type data. """
    question_type_service = QuestionTypeService(db)
    question_type = await question_type_service.create(payload)
    return question_type


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_question_type(
    payload: QuestionTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update question type data. """
    question_type_service = QuestionTypeService(db)
    await question_type_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutQuestionTypeSchema
)
async def get_question_type(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutQuestionTypeSchema:
    """ api to get question type data by id. """
    question_type_service = QuestionTypeService(db)
    question_type = await question_type_service.get_by_id(uuid)
    return question_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_question_type(db: AsyncSession = Depends(get_db)):
    """ api to get question type data. """
    question_type_service = QuestionTypeService(db)
    question_type = await question_type_service.get_all()
    return question_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_question_type(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete question type data by id. """
    question_type_service = QuestionTypeService(db)
    await question_type_service.delete(uuid)


@router.get("/module/type", status_code=status.HTTP_200_OK)
async def get_question_by_module_type(
    module_Type: int, db: AsyncSession = Depends(get_db)
):
    """ api to get question type data by module type. """
    question_type_service = QuestionTypeService(db)
    question_type = await question_type_service.get_by_type(module_Type)
    return question_type


