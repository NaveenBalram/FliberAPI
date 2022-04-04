import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.user_answers import UserAnswersRepository
from app.models.schema.user_answers import (
    InUserAnswersSchema,
    UserAnswersSchema,
)

logger = logging.getLogger(__name__)


class UserAnswersService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._user_answers_repository = UserAnswersRepository(self._db_session)

    async def create(self, payload: InUserAnswersSchema):
        user_answers = await self._user_answers_repository.create(payload)

        return user_answers

    async def get_by_id(self, uuid: UUID):
        user_answers = await self._user_answers_repository.get_by_id(uuid)
        return user_answers

    async def get_all(self):
        user_answers = await self._user_answers_repository.get_all()
        return user_answers

    async def delete(self, uuid: UUID):
        await self._user_answers_repository.delete(uuid)

    async def update(self, payload: UserAnswersSchema):
        await self._user_answers_repository.update(payload)

    async def delete_user_answers_by_user_id(self, user_id: UUID):
        await self._user_answers_repository.delete_by_user_id(user_id)
