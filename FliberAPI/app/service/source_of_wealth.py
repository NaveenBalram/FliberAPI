import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.source_of_wealth import SourceOfWealthRepository
from app.models.schema.source_of_wealth import (
    InSourceOfWealthSchema,
    SourceOfWealthSchema,
)

logger = logging.getLogger(__name__)


class SourceOfWealthService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._source_of_wealth_repository = SourceOfWealthRepository(self._db_session)

    async def create(self, payload: InSourceOfWealthSchema):
        source_of_wealth = await self._source_of_wealth_repository.create(payload)

        return source_of_wealth

    async def get_by_id(self, uuid: UUID):
        source_of_wealth = await self._source_of_wealth_repository.get_by_id(uuid)
        return source_of_wealth

    async def get_all(self):
        source_of_wealth = await self._source_of_wealth_repository.get_all()
        return source_of_wealth

    async def delete(self, uuid: UUID):
        await self._source_of_wealth_repository.delete(uuid)

    async def update(self, payload: SourceOfWealthSchema):
        await self._source_of_wealth_repository.update(payload)

    async def delete_source_of_wealth_by_user_id(self, user_id: UUID):
        await self._source_of_wealth_repository.delete_by_user_id(user_id)
