from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class NetWorthFrequencyTypeDataSchemaBase(BaseSchema):
    Name: str
    Months: int
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthFrequencyTypeDataSchema(NetWorthFrequencyTypeDataSchemaBase):
    Id: UUID


class InNetWorthFrequencyTypeDataSchema(NetWorthFrequencyTypeDataSchemaBase):
    ...


class OutNetWorthFrequencyTypeDataSchema(NetWorthFrequencyTypeDataSchema):
    ...
