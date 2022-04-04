import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.asset_type import AssetTypeRepository
from app.models.schema.asset_type import (
    InAssetTypeSchema,
    AssetTypeSchema,
)

logger = logging.getLogger(__name__)


class AssetTypeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._asset_type_repository = AssetTypeRepository(self._db_session)

    async def create(self, payload: InAssetTypeSchema):
        asset_type = await self._asset_type_repository.create(payload)

        return asset_type

    async def get_by_id(self, uuid: UUID):
        asset_type = await self._asset_type_repository.get_by_id(uuid)
        return asset_type

    async def get_all(self):
        asset_type = await self._asset_type_repository.get_all()
        return asset_type

    async def delete(self, uuid: UUID):
        await self._asset_type_repository.delete(uuid)

    async def update(self, payload: AssetTypeSchema):
        await self._asset_type_repository.update(payload)

    async def delete_asset_type_by_user_id(self, user_id: UUID):
        await self._asset_type_repository.delete_by_user_id(user_id)
