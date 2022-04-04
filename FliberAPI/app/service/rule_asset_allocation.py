import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from app.db.repositories.rule_asset_allocation import RuleAssetAllocationRepository
from app.models.schema.rule_asset_allocation import (
    RuleAssetAllocationSchema,
    RuleAssetAllocationSchemaBase,
)

logger = logging.getLogger(__name__)


class RuleAssetAllocationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session

    async def create(
            self, payload: RuleAssetAllocationSchema
    ):
        rule_asset_allocation_repository = RuleAssetAllocationRepository(self._db_session)
        rule_asset_allocation_repository = await rule_asset_allocation_repository.create(payload)

        return rule_asset_allocation_repository

    async def get_by_id(self, uuid: UUID):
        rule_asset_allocation_repository = RuleAssetAllocationRepository(self._db_session)
        rule_asset_allocation_repository = await rule_asset_allocation_repository.get_by_id(uuid)
        return rule_asset_allocation_repository

    async def get_all(self):
        rule_asset_allocation_repository = RuleAssetAllocationRepository(self._db_session)
        rule_asset_allocation_repository = await rule_asset_allocation_repository.get_all()
        return rule_asset_allocation_repository

    async def delete(self, uuid: UUID):
        rule_asset_allocation_repository = RuleAssetAllocationRepository(self._db_session)
        await rule_asset_allocation_repository.delete(uuid)

    async def update(self, payload: RuleAssetAllocationSchema):
        rule_asset_allocation_repository = RuleAssetAllocationRepository(self._db_session)
        await rule_asset_allocation_repository.update(payload)

