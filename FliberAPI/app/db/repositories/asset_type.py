from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.asset_type import AssetType
from app.models.schema.asset_type import (
    AssetTypeSchemaBase,
    AssetTypeSchema,
    InAssetTypeSchema,
)


class AssetTypeRepository(
    BaseRepository[AssetTypeSchemaBase, AssetTypeSchema, AssetType]
):
    @property
    def _in_schema(self) -> Type[AssetTypeSchemaBase]:
        return InAssetTypeSchema

    @property
    def _schema(self) -> Type[AssetTypeSchema]:
        return AssetTypeSchema

    @property
    def _table(self) -> Type[AssetType]:
        return AssetType
