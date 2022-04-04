import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.choice import ChoiceRepository
from app.db.repositories.question_type import QuestionTypeRepository
from app.models.schema.question_type import (
    InQuestionTypeSchema,
    QuestionTypeSchema,
)

logger = logging.getLogger(__name__)


class QuestionTypeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._question_type_repository = QuestionTypeRepository(self._db_session)

    async def create(self, payload: InQuestionTypeSchema):
        question_type = await self._question_type_repository.create(payload)

        return question_type

    async def get_by_id(self, uuid: UUID):
        question_type = await self._question_type_repository.get_by_id(uuid)
        return question_type

    async def get_all(self):
        question_type = await self._question_type_repository.get_all()
        return question_type

    async def delete(self, uuid: UUID):
        await self._question_type_repository.delete(uuid)

    async def update(self, payload: QuestionTypeSchema):
        await self._question_type_repository.update(payload)

    async def get_by_name(self, name: str):
        await self._question_type_repository.get_by_name(name)

    async def get_by_type(self, module_type: int):
        result = await self._question_type_repository.get_by_type(module_type)

        return_items = []
        for question in result:
            choices = []
            if module_type == 2:
                choice_repository = ChoiceRepository(self._db_session)
                choices = await choice_repository.get_by_question_id(question["Id"])
            question["Choices"] = choices
            return_items.append(question)

        print("len", len(return_items))
        return return_items

    async def delete_question_type_by_user_id(self, user_id: UUID):
        await self._question_type_repository.delete_by_user_id(user_id)
