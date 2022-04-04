import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.post_retirement_configuration import (
    PostRetirementConfigurationRepository,
)
from app.models.schema.post_retirement_configuration import (
    OutPostRetirementConfigurationSchema,
    InPostRetirementConfigurationSchema,
    PostRetirementConfigurationSchema,
)

logger = logging.getLogger(__name__)


class PostRetirementConfigurationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._post_retirement_configuration_repository = PostRetirementConfigurationRepository(self._db_session)

    async def create(
            self, payload: InPostRetirementConfigurationSchema
    ):
        post_retirement_configuration = (
            await self._post_retirement_configuration_repository.create(payload)
        )

        return post_retirement_configuration

    async def get_by_id(self, uuid: UUID) -> OutPostRetirementConfigurationSchema:
        post_retirement_configuration = (
            await self._post_retirement_configuration_repository.get_by_id(uuid)
        )
        return post_retirement_configuration

    async def get_all(self):
        post_retirement_configuration = (
            await self._post_retirement_configuration_repository.get_all()
        )
        return post_retirement_configuration

    async def delete(self, uuid: UUID):
        await self._post_retirement_configuration_repository.delete(uuid)

    async def update(self, payload: PostRetirementConfigurationSchema):
        await self._post_retirement_configuration_repository.update(payload)

    async def delete_post_retirement_configuration_by_user_id(self, user_id: UUID):
        await self._post_retirement_configuration_repository.delete_by_user_id(user_id)
