import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.assets_limit import AssetsLimitRepository
from app.models.schema.assets_limit import (
    AssetsLimitSchema,
    InAssetsLimitSchema,
)

logger = logging.getLogger(__name__)


class AssetsLimitService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._assets_limit_repository = AssetsLimitRepository(self._db_session)

    async def create(self, payload: InAssetsLimitSchema):
        assets_limit = await self._assets_limit_repository.create(payload)
        return assets_limit

    async def get_by_id(self, uuid: UUID):
        assets_limit = await self._assets_limit_repository.get_by_id(uuid)
        return assets_limit

    async def get_all(self):
        assets_limit = await self._assets_limit_repository.get_all()
        return assets_limit

    async def delete(self, uuid: UUID):
        await self._assets_limit_repository.delete(uuid)

    async def update(self, payload: AssetsLimitSchema):
        await self._assets_limit_repository.update(payload)
