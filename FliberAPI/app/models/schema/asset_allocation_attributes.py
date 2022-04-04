from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class AssetAllocationAttributesSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class AssetAllocationAttributesSchema(AssetAllocationAttributesSchemaBase):
    Id: UUID


class InAssetAllocationAttributesSchema(AssetAllocationAttributesSchemaBase):
    ...


class OutAssetAllocationAttributesSchema(AssetAllocationAttributesSchema):
    ...
