import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.sustainability_score_configuration import (
    SustainabilityScoreConfigurationRepository,
)
from app.models.schema.sustainability_score_configuration import (
    InSustainabilityScoreConfigurationSchema,
    SustainabilityScoreConfigurationSchema,
)

logger = logging.getLogger(__name__)


class SustainabilityScoreConfigurationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._sustainability_score_configuration_repository = SustainabilityScoreConfigurationRepository(
            self._db_session)

    async def create(
            self, payload: InSustainabilityScoreConfigurationSchema
    ):
        sustainability_score_configuration = (
            await self._sustainability_score_configuration_repository.create(payload)
        )

        return sustainability_score_configuration

    async def get_by_id(self, uuid: UUID):
        sustainability_score_configuration = (
            await self._sustainability_score_configuration_repository.get_by_id(uuid)
        )
        return sustainability_score_configuration

    async def get_all(self):
        sustainability_score_configuration = (
            await self._sustainability_score_configuration_repository.get_all()
        )
        return sustainability_score_configuration

    async def delete(self, uuid: UUID):
        await self._sustainability_score_configuration_repository.delete(uuid)

    async def update(self, payload: SustainabilityScoreConfigurationSchema):
        await self._sustainability_score_configuration_repository.update(payload)

    async def delete_sustainability_score_configuration_by_user_id(self, user_id: UUID):
        await self._sustainability_score_configuration_repository.delete_by_user_id(user_id)
