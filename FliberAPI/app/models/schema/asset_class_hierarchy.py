from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class AssetClassHierarchySchemaBase(BaseSchema):
    assetClass: str
    assetType: str
    CreatedOn: datetime


class AssetClassHierarchySchema(AssetClassHierarchySchemaBase):
    Id: UUID


class InAssetClassHierarchySchema(AssetClassHierarchySchemaBase):
    ...


class OutAssetClassHierarchySchema(AssetClassHierarchySchema):
    ...
