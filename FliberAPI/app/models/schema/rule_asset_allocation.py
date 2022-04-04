from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class RuleAssetAllocationSchemaBase(BaseSchema):
    RuleId: UUID
    assetType: str
    AllocationPercentage: float
    CreatedOn: datetime


class RuleAssetAllocationSchema(RuleAssetAllocationSchemaBase):
    Id: UUID


class InRuleAssetAllocationSchema(RuleAssetAllocationSchemaBase):
    ...


class OutRuleAssetAllocationSchema(RuleAssetAllocationSchema):
    ...
