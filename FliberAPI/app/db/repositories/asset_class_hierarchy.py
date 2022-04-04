from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.asset_class_hierarchy import AssetClassHierarchy
from app.models.schema.asset_class_hierarchy import AssetClassHierarchySchema, AssetClassHierarchySchemaBase


class AssetClassHierarchyRepository(
    BaseRepository[AssetClassHierarchySchema, AssetClassHierarchySchemaBase, AssetClassHierarchy]):
    @property
    def _in_schema(self) -> Type[AssetClassHierarchySchema]:
        return AssetClassHierarchySchema

    @property
    def _schema(self) -> Type[AssetClassHierarchySchemaBase]:
        return AssetClassHierarchySchemaBase

    @property
    def _table(self) -> Type[AssetClassHierarchy]:
        return AssetClassHierarchy
