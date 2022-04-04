import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.ability_configuration import AbilityConfigurationRepository
from app.models.schema.ability_configuration import (
    InAbilityConfigurationSchema,
    AbilityConfigurationSchema,
)

logger = logging.getLogger(__name__)


class AbilityConfigurationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._ability_configuration_repository = AbilityConfigurationRepository(
            self._db_session
        )

    async def create(
            self, payload: InAbilityConfigurationSchema
    ):
        ability_configuration = await self._ability_configuration_repository.create(payload)
        return ability_configuration

    async def get_by_id(self, uuid: UUID):
        ability_configuration = await self._ability_configuration_repository.get_by_id(uuid)
        return ability_configuration

    async def get_all(self):
        ability_configuration = await self._ability_configuration_repository.get_all()
        return ability_configuration

    async def delete(self, uuid: UUID):
        await self._ability_configuration_repository.delete(uuid)

    async def update(self, payload: AbilityConfigurationSchema):
        await self._ability_configuration_repository.update(payload)

    async def delete_by_user_id(self, user_id: UUID):
        await self._ability_configuration_repository.delete_by_user_id(user_id)

    async def delete_ability_configuration_by_user_id(self, user_id: UUID):
        await self._ability_configuration_repository.delete_by_user_id(user_id)
