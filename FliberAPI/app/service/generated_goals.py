import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.generated_goals import GeneratedGoalsRepository
from app.models.schema.generated_goals import (
    InGeneratedGoalsSchema,
    GeneratedGoalsSchema,
)

logger = logging.getLogger(__name__)


class GeneratedGoalsService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._generated_goals_repository = GeneratedGoalsRepository(self._db_session)

    async def create(self, payload: InGeneratedGoalsSchema):
        generated_goals = await self._generated_goals_repository.create(payload)

        return generated_goals

    async def get_by_id(self, uuid: UUID):
        generated_goals = await self._generated_goals_repository.get_by_id(uuid)
        return generated_goals

    async def get_all(self):
        generated_goals = await self._generated_goals_repository.get_all()
        return generated_goals

    async def delete(self, uuid: UUID):
        await self._generated_goals_repository.delete(uuid)

    async def update(self, payload: GeneratedGoalsSchema):
        await self._generated_goals_repository.update(payload)

    async def bulk_insert(self, payload: list):
        await self._generated_goals_repository.bulk_insert(payload)

    async def delete_generated_goals_by_user_id(self, user_id: UUID):
        await self._generated_goals_repository.delete_by_user_id(user_id)
