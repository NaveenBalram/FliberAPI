from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class AssetsLimitSchemaBase(BaseSchema):

    AssetTypeId: UUID
    AssetLowerLimit: float
    AssetUpperLimit: float
    AssetCrossLimit: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool


class AssetsLimitSchema(AssetsLimitSchemaBase):
    Id: UUID


class InAssetsLimitSchema(AssetsLimitSchemaBase):
    ...


class OutAssetsLimitSchema(AssetsLimitSchema):
    ...
