import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.asset_allocation_attributes import (
    AssetAllocationAttributesRepository,
)
from app.models.schema.asset_allocation_attributes import (
    OutAssetAllocationAttributesSchema,
    InAssetAllocationAttributesSchema,
    AssetAllocationAttributesSchema,
)

logger = logging.getLogger(__name__)


class AssetAllocationAttributesService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._asset_allocation_attributes_repository = AssetAllocationAttributesRepository(
            self._db_session
        )

    async def create(
            self, payload: InAssetAllocationAttributesSchema
    ):
        asset_allocation_attributes = (
            await self._asset_allocation_attributes_repository.create(payload)
        )

        return asset_allocation_attributes

    async def get_by_id(self, uuid: UUID):
        asset_allocation_attributes = (
            await self._asset_allocation_attributes_repository.get_by_id(uuid)
        )
        return OutAssetAllocationAttributesSchema(**asset_allocation_attributes.dict())

    async def get_all(self):
        asset_allocation_attributes = (
            await self._asset_allocation_attributes_repository.get_all()
        )
        return asset_allocation_attributes

    async def delete(self, uuid: UUID):
        await self._asset_allocation_attributes_repository.delete(uuid)

    async def update(self, payload: AssetAllocationAttributesSchema):
        await self._asset_allocation_attributes_repository.update(payload)

    async def delete_asset_allocation_attributes_by_user_id(self, user_id: UUID):
        await self._asset_allocation_attributes_repository.delete_by_user_id(user_id)
