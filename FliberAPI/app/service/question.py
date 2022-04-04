import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.choice import ChoiceRepository
from app.db.repositories.question import QuestionRepository
from app.models.schema.question import (
    InQuestionSchema,
    QuestionSchema,
)

logger = logging.getLogger(__name__)


class QuestionService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._question_repository = QuestionRepository(self._db_session)

    async def create(self, payload: InQuestionSchema):
        question = await self._question_repository.create(payload)

        return question

    async def get_by_id(self, uuid: UUID):
        question = await self._question_repository.get_by_id(uuid)
        return question

    async def get_all(self):
        question = await self._question_repository.get_all()
        return question

    async def delete(self, uuid: UUID):
        await self._question_repository.delete(uuid)

    async def update(self, payload: QuestionSchema):
        await self._question_repository.update(payload)

    async def question_info(self, module_type: int):
        """ Fetch the question based on the module type passed. """

        if module_type == "1":
            questions = await self._question_repository.question_info(ref_id1=3)
        elif module_type == "3":
            questions = await self._question_repository.question_info(ref_id1=4)
        else:
            questions = await self._question_repository.question_info(ref_id1=1, ref_id2=2)

        result = []

        choice_repository = ChoiceRepository(self._db_session)

        for data in questions:
            result.append(
                {
                    "questionTitle": data.questionTitle,
                    "description": data.description,
                    "questionTypeId": data.questionTypeId,
                    "questionSequence": data.questionSequence,
                    "questionId": data.Id,
                    "totalQuestions": len(questions),
                    "prevQuestionId": 0
                    if data.id == 14 | data.id == 22
                    else data.id - 1,
                    "choices": []
                    if module_type == "1" or "3"
                    else choice_repository.get_by_question_id(data.id),
                }
            )

        return result

    async def delete_question_by_user_id(self, user_id: UUID):
        await self._question_repository.delete_by_user_id(user_id)
