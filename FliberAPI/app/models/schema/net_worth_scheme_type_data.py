from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class NetWorthSchemeTypeDataSchemaBase(BaseSchema):
    Name: str
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthSchemeTypeDataSchema(NetWorthSchemeTypeDataSchemaBase):
    Id: UUID


class InNetWorthSchemeTypeDataSchema(NetWorthSchemeTypeDataSchemaBase):
    ...


class OutNetWorthSchemeTypeDataSchema(NetWorthSchemeTypeDataSchema):
    ...
