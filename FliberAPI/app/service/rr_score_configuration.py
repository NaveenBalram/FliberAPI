import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.rr_score_configuration import RrScoreConfigurationRepository
from app.models.schema.rr_score_configuration import (
    InRrScoreConfigurationSchema,
    RrScoreConfigurationSchema,
)

logger = logging.getLogger(__name__)


class RrScoreConfigurationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._rr_score_configuration_repository = RrScoreConfigurationRepository(self._db_session)

    async def create(
            self, payload: InRrScoreConfigurationSchema
    ):
        rr_score_configuration = await self._rr_score_configuration_repository.create(payload)

        return rr_score_configuration

    async def get_by_id(self, uuid: UUID):
        rr_score_configuration = await self._rr_score_configuration_repository.get_by_id(uuid)
        return rr_score_configuration

    async def get_all(self):
        rr_score_configuration = await self._rr_score_configuration_repository.get_all()
        return rr_score_configuration

    async def delete(self, uuid: UUID):
        await self._rr_score_configuration_repository.delete(uuid)

    async def update(self, payload: RrScoreConfigurationSchema):
        await self._rr_score_configuration_repository.update(payload)

    async def delete_rr_score_configuration_by_user_id(self, user_id: UUID):
        await self._rr_score_configuration_repository.delete_by_user_id(user_id)
