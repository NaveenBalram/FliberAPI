import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.willingness_configuration import (
    WillingnessConfigurationRepository,
)
from app.models.schema.willingness_configuration import (
    InWillingnessConfigurationSchema,
    WillingnessConfigurationSchema,
)

logger = logging.getLogger(__name__)


class WillingnessConfigurationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._willingness_configuration_repository = WillingnessConfigurationRepository(self._db_session)

    async def create(
            self, payload: InWillingnessConfigurationSchema
    ):
        willingness_configuration = await self._willingness_configuration_repository.create(
            payload
        )

        return willingness_configuration

    async def get_by_id(self, uuid: UUID):
        willingness_configuration = (
            await self._willingness_configuration_repository.get_by_id(uuid)
        )
        return willingness_configuration

    async def get_all(self):
        willingness_configuration = await self._willingness_configuration_repository.get_all()
        return willingness_configuration

    async def delete(self, uuid: UUID):
        await self._willingness_configuration_repository.delete(uuid)

    async def update(self, payload: WillingnessConfigurationSchema):
        await self._willingness_configuration_repository.update(payload)

    async def delete_willingness_configuration_by_user_id(self, user_id: UUID):
        await self._willingness_configuration_repository.delete_by_user_id(user_id)
