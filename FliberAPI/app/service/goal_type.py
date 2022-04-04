import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.goal_type import GoalTypeRepository
from app.models.schema.goal_type import (
    InGoalTypeSchema,
    GoalTypeSchema,
)

logger = logging.getLogger(__name__)


class GoalTypeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._goal_type_repository = GoalTypeRepository(self._db_session)

    async def create(self, payload: InGoalTypeSchema):
        goal_type = await self._goal_type_repository.create(payload)

        return goal_type

    async def get_by_id(self, uuid: UUID):
        goal_type = await self._goal_type_repository.get_by_id(uuid)
        return goal_type

    async def get_all(self):
        goal_type = await self._goal_type_repository.get_all()
        return goal_type

    async def delete(self, uuid: UUID):
        await self._goal_type_repository.delete(uuid)

    async def update(self, payload: GoalTypeSchema):
        await self._goal_type_repository.update(payload)

    async def delete_goal_type_by_user_id(self, user_id: UUID):
        await self._goal_type_repository.delete_by_user_id(user_id)
