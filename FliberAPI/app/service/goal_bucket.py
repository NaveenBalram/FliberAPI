import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.goal_bucket import GoalBucketRepository
from app.models.schema.goal_bucket import (
    InGoalBucketSchema,
    GoalBucketSchema,
)

logger = logging.getLogger(__name__)


class GoalBucketService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._goal_bucket_repository = GoalBucketRepository(self._db_session)

    async def create(self, payload: InGoalBucketSchema):
        goal_bucket = await self._goal_bucket_repository.create(payload)

        return goal_bucket

    async def get_by_id(self, uuid: UUID):
        goal_bucket = await self._goal_bucket_repository.get_by_id(uuid)
        return goal_bucket

    async def get_all(self):
        goal_bucket = await self._goal_bucket_repository.get_all()
        return goal_bucket

    async def delete(self, uuid: UUID):
        await self._goal_bucket_repository.delete(uuid)

    async def update(self, payload: GoalBucketSchema):
        await self._goal_bucket_repository.update(payload)

    async def delete_goal_bucket_by_user_id(self, user_id: UUID):
        await self._goal_bucket_repository.delete_by_user_id(user_id)
