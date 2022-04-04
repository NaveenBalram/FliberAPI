from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class AssetTypeSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    # AssetLiabilityCategoryId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class AssetTypeSchema(AssetTypeSchemaBase):
    Id: UUID


class InAssetTypeSchema(AssetTypeSchemaBase):
    ...


class OutAssetTypeSchema(AssetTypeSchema):
    ...
