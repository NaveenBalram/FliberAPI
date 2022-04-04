import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.risk_profile_configuration import (
    RiskProfileConfigurationRepository,
)
from app.models.schema.risk_profile_configuration import (
    InRiskProfileConfigurationSchema,
    RiskProfileConfigurationSchema,
)

logger = logging.getLogger(__name__)


class RiskProfileConfigurationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._risk_profile_configuration_repository = RiskProfileConfigurationRepository(self._db_session)

    async def create(
            self, payload: InRiskProfileConfigurationSchema
    ):
        risk_profile_configuration = await self._risk_profile_configuration_repository.create(
            payload
        )

        return risk_profile_configuration

    async def get_by_id(self, uuid: UUID):
        risk_profile_configuration = (
            await self._risk_profile_configuration_repository.get_by_id(uuid)
        )
        return risk_profile_configuration

    async def get_all(self):
        risk_profile_configuration = (
            await self._risk_profile_configuration_repository.get_all()
        )
        return risk_profile_configuration

    async def delete(self, uuid: UUID):
        await self._risk_profile_configuration_repository.delete(uuid)

    async def update(self, payload: RiskProfileConfigurationSchema):
        await self._risk_profile_configuration_repository.update(payload)

    async def delete_risk_profile_configuration_by_user_id(self, user_id: UUID):
        await self._risk_profile_configuration_repository.delete_by_user_id(user_id)
