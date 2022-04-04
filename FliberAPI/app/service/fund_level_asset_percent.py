import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.fund_level_asset_percent import FundLevelAssetPercentRepository
from app.models.schema.fund_level_asset_percent import (
    OutFundLevelAssetPercentSchema,
    FundLevelAssetPercentSchema,
    InFundLevelAssetPercentSchema,
)

logger = logging.getLogger(__name__)


class FundLevelAssetPercentService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._fund_level_asset_percent_repository = FundLevelAssetPercentRepository(self._db_session)

    async def create(
            self, payload: InFundLevelAssetPercentSchema
    ):
        fund_level_asset_percent = await self._fund_level_asset_percent_repository.create(
            payload
        )

        return fund_level_asset_percent

    async def get_by_id(self, uuid: UUID) -> OutFundLevelAssetPercentSchema:
        fund_level_asset_percent = await self._fund_level_asset_percent_repository.get_by_id(
            uuid
        )
        return fund_level_asset_percent

    async def get_all(self):
        fund_level_asset_percent = await self._fund_level_asset_percent_repository.get_all()
        return fund_level_asset_percent

    async def delete(self, uuid: UUID):
        await self._fund_level_asset_percent_repository.delete(uuid)

    async def update(self, payload: FundLevelAssetPercentSchema):
        await self._fund_level_asset_percent_repository.update(payload)
