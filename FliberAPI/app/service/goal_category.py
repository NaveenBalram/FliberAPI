import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.goal_category import GoalCategoryRepository
from app.models.schema.goal_category import (
    InGoalCategorySchema,
    GoalCategorySchema,
)

logger = logging.getLogger(__name__)


class GoalCategoryService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._goal_category_repository = GoalCategoryRepository(self._db_session)

    async def create(self, payload: InGoalCategorySchema):
        goal_category = await self._goal_category_repository.create(payload)

        return goal_category

    async def get_by_id(self, uuid: UUID):
        goal_category = await self._goal_category_repository.get_by_id(uuid)
        return goal_category

    async def get_all(self):
        goal_category = await self._goal_category_repository.get_all()
        return goal_category

    async def delete(self, uuid: UUID):
        await self._goal_category_repository.delete(uuid)

    async def update(self, payload: GoalCategorySchema):
        await self._goal_category_repository.update(payload)

    async def delete_goal_category_by_user_id(self, user_id: UUID):
        await self._goal_category_repository.delete_by_user_id(user_id)
