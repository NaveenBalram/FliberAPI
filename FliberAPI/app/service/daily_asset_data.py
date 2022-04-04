import logging

from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.daily_asset_data import DailyAssetDataRepository
from app.models.schema.daily_asset_data import (
    OutDailyAssetDataSchema,
    DailyAssetDataSchema,
    InDailyAssetDataSchema,
)

logger = logging.getLogger(__name__)


class DailyAssetDataService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._daily_asset_data_repository = DailyAssetDataRepository(self._db_session)

    async def create(self, payload: InDailyAssetDataSchema):
        daily_asset_data = await self._daily_asset_data_repository.create(payload)

        return daily_asset_data

    async def get_by_id(self, uuid: UUID):
        daily_asset_data = await self._daily_asset_data_repository.get_by_id(uuid)
        return daily_asset_data

    async def get_all(self):
        daily_asset_data = await self._daily_asset_data_repository.get_all()
        return daily_asset_data

    async def delete(self, uuid: UUID):
        await self._daily_asset_data_repository.delete(uuid)

    async def delete_by_user_id(self, uuid: UUID):
        await self._daily_asset_data_repository.delete_by_user_id(uuid)

    async def update(self, payload: DailyAssetDataSchema):
        await self._daily_asset_data_repository.update(payload)
