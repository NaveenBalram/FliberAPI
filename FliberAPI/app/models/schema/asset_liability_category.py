from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class AssetLiabilityCategorySchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class AssetLiabilityCategorySchema(AssetLiabilityCategorySchemaBase):
    Id: UUID


class InAssetLiabilityCategorySchema(AssetLiabilityCategorySchemaBase):
    ...


class OutAssetLiabilityCategorySchema(AssetLiabilityCategorySchema):
    ...
