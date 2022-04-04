import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.user_result import UserResultRepository
from app.models.schema.user_result import (
    InUserResultSchema,
    UserResultSchema,
)

logger = logging.getLogger(__name__)


class UserResultService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._user_result_repository = UserResultRepository(self._db_session)

    async def create(self, payload: InUserResultSchema):
        user_result = await self._user_result_repository.create(payload)

        return user_result

    async def get_by_id(self, uuid: UUID):
        user_result = await self._user_result_repository.get_by_id(uuid)
        return user_result

    async def get_all(self):
        user_result = await self._user_result_repository.get_all()
        return user_result

    async def delete(self, uuid: UUID):
        await self._user_result_repository.delete(uuid)

    async def update(self, payload: UserResultSchema):
        await self._user_result_repository.update(payload)

    async def delete_user_result_by_user_id(self, user_id: UUID):
        await self._user_result_repository.delete_by_user_id(user_id)
