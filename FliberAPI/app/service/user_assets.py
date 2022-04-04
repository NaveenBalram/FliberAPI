import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.user_assets import UserAssetsRepository
from app.models.schema.user_assets import (
    InUserAssetsSchema,
    UserAssetsSchema,
)

logger = logging.getLogger(__name__)


class UserAssetsService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._user_assets_repository = UserAssetsRepository(self._db_session)

    async def create(self, payload: InUserAssetsSchema):
        user_assets = await self._user_assets_repository.create(payload)

        return user_assets

    async def get_by_id(self, uuid: UUID):
        user_assets = await self._user_assets_repository.get_by_id(uuid)
        return user_assets

    async def get_all(self):
        user_assets = await self._user_assets_repository.get_all()
        return user_assets

    async def delete(self, uuid: UUID):
        await self._user_assets_repository.delete(uuid)

    async def update(self, payload: UserAssetsSchema):
        await self._user_assets_repository.update(payload)
