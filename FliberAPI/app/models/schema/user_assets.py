from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class UserAssetsSchemaBase(BaseSchema):

    UserId: UUID
    AssetTypeId: UUID
    FundName: str
    NoOfUnits: int
    CreatedOn: datetime
    UpdatedOn: datetime


class UserAssetsSchema(UserAssetsSchemaBase):
    Id: UUID


class InUserAssetsSchema(UserAssetsSchemaBase):
    ...


class OutUserAssetsSchema(UserAssetsSchema):
    ...
