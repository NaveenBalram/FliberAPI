import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.pre_retirement_configuration import (
    PreRetirementConfigurationRepository,
)
from app.models.schema.pre_retirement_configuration import (
    InPreRetirementConfigurationSchema,
    PreRetirementConfigurationSchema,
)

logger = logging.getLogger(__name__)


class PreRetirementConfigurationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._pre_retirement_configuration_repository = PreRetirementConfigurationRepository(self._db_session)
        self.pre_retirement_configuration_repository = (
            PreRetirementConfigurationRepository(self._db_session)
        )

    async def create(
            self, payload: InPreRetirementConfigurationSchema
    ):
        pre_retirement_configuration = (
            await self.pre_retirement_configuration_repository.create(payload)
        )
        return pre_retirement_configuration

    async def get_by_id(self, uuid: UUID):
        pre_retirement_configuration = (
            await self.pre_retirement_configuration_repository.get_by_id(uuid)
        )
        return pre_retirement_configuration

    async def get_all(self):
        return await self.pre_retirement_configuration_repository.get_all()

    async def delete(self, uuid: UUID):
        return await self.pre_retirement_configuration_repository.delete(uuid)

    async def update(self, payload: PreRetirementConfigurationSchema):
        return await self.pre_retirement_configuration_repository.update(payload)

    async def delete_pre_retirement_configuration_by_user_id(self, user_id: UUID):
        return await self.pre_retirement_configuration_repository.delete_by_user_id(
            user_id
        )
