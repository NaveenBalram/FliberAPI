import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from app.db.repositories.asset_class_hierarchy import AssetClassHierarchyRepository
from app.models.schema.asset_class_hierarchy import (
    AssetClassHierarchySchemaBase,
    AssetClassHierarchySchema,
)

logger = logging.getLogger(__name__)


class AssetClassHierarchyService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session

    async def create(
            self, payload: AssetClassHierarchySchema
    ):
        asset_class_hierarchy = AssetClassHierarchyRepository(self._db_session)
        asset_class_hierarchy = await asset_class_hierarchy.create(payload)

        return asset_class_hierarchy

    async def get_by_id(self, uuid: UUID):
        asset_class_hierarchy = AssetClassHierarchyRepository(self._db_session)
        asset_class_hierarchy = await asset_class_hierarchy.get_by_id(uuid)
        return asset_class_hierarchy

    async def get_all(self):
        asset_class_hierarchy = AssetClassHierarchyRepository(self._db_session)
        asset_class_hierarchy = await asset_class_hierarchy.get_all()
        return asset_class_hierarchy

    async def delete(self, uuid: UUID):
        asset_class_hierarchy = AssetClassHierarchyRepository(self._db_session)
        await asset_class_hierarchy.delete(uuid)

    async def update(self, payload: AssetClassHierarchySchema):
        asset_class_hierarchy = asset_class_hierarchy(self._db_session)
        await asset_class_hierarchy.update(payload)

