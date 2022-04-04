import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.submit_question import SubmitQuestionRepository
from app.models.schema.submit_question import (
    InSubmitQuestionSchema,
    SubmitQuestionSchema,
    SubmitQuestionSchemaBase,
)

logger = logging.getLogger(__name__)


class SubmitQuestionService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._submit_question_repository = SubmitQuestionRepository(self._db_session)

    async def create(self, payload: InSubmitQuestionSchema):
        submit_question = await self._submit_question_repository.create(payload)

        return submit_question

    async def get_by_id(self, uuid: UUID):
        submit_question = await self._submit_question_repository.get_by_id(uuid)
        return submit_question

    async def get_all(self):
        submit_question = await self._submit_question_repository.get_all()
        return submit_question

    async def delete(self, uuid: UUID):
        await self._submit_question_repository.delete(uuid)

    async def update(self, payload: SubmitQuestionSchema):
        await self._submit_question_repository.update(payload)

    async def get_value_by(self, payload: dict):
        await self._submit_question_repository.get_by_value(payload)

    async def bulk_create(self, payload: list[SubmitQuestionSchemaBase]):
        submit_question = await self._submit_question_repository.bulk_create(payload)
        return submit_question

    async def delete_submit_question_by_user_id(self, user_id: UUID):
        await self._submit_question_repository.delete_by_user_id(user_id)
