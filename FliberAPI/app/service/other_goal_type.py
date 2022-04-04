import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.other_goal_type import OtherGoalTypeRepository
from app.models.schema.other_goal_type import (
    InOtherGoalTypeSchema,
    OtherGoalTypeSchema,
)

logger = logging.getLogger(__name__)


class OtherGoalTypeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._other_goal_type_repository = OtherGoalTypeRepository(self._db_session)

    async def create(self, payload: InOtherGoalTypeSchema):
        other_goal_type = await self._other_goal_type_repository.create(payload)

        return other_goal_type

    async def get_by_id(self, uuid: UUID):
        other_goal_type = await self._other_goal_type_repository.get_by_id(uuid)
        return other_goal_type

    async def get_all(self):
        other_goal_type = await self._other_goal_type_repository.get_all()
        return other_goal_type

    async def delete(self, uuid: UUID):
        await self._other_goal_type_repository.delete(uuid)

    async def update(self, payload: OtherGoalTypeSchema):
        await self._other_goal_type_repository.update(payload)

    async def delete_other_goal_type_by_user_id(self, user_id: UUID):
        await self._other_goal_type_repository.delete_by_user_id(user_id)
