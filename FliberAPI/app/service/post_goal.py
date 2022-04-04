import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.post_goal import PostGoalRepository
from app.models.schema.post_goal import (
    InPostGoalSchema,
    PostGoalSchema,
)

logger = logging.getLogger(__name__)


class PostGoalService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._post_goal_repository = PostGoalRepository(self._db_session)

    async def create(self, payload: InPostGoalSchema):
        post_goal = await self._post_goal_repository.create(payload)

        return post_goal

    async def get_by_id(self, uuid: UUID):
        post_goal = await self._post_goal_repository.get_by_id(uuid)
        return post_goal

    async def get_all(self):
        post_goal = await self._post_goal_repository.get_all()
        return post_goal

    async def delete(self, uuid: UUID):
        await self._post_goal_repository.delete(uuid)

    async def update(self, payload: PostGoalSchema):
        await self._post_goal_repository.update(payload)

    async def delete_post_goal_by_user_id(self, user_id: UUID):
        await self._post_goal_repository.delete_by_user_id(user_id)
