import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.user_goals import UserGoalsRepository
from app.models.schema.user_goals import (
    UserGoalsSchema,
    UserGoalsSchemaBase,
)

logger = logging.getLogger(__name__)


class UserGoalsService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._user_goals_repository = UserGoalsRepository(self._db_session)

    async def create(self, payload: UserGoalsSchemaBase):
        user_goals = await self._user_goals_repository.create(payload)
        return user_goals

    async def get_by_id(self, uuid: UUID):
        user_goals = await self._user_goals_repository.get_by_id(uuid)
        return user_goals

    async def get_all(self):
        user_goals = await self._user_goals_repository.get_all()
        return user_goals

    async def delete(self, uuid: UUID):
        await self._user_goals_repository.delete(uuid)

    async def update(self, payload: UserGoalsSchema):
        await self._user_goals_repository.update(payload)

    async def get_by_user_id(self, user_id: UUID):
        return await self._user_goals_repository.get_user_goal_by_id(user_id)

    async def delete_user_goals_by_user_id(self, user_id: UUID):
        await self._user_goals_repository.delete_by_user_id(user_id)
