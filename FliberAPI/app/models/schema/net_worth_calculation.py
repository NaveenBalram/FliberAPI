from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class NetWorthCalculationSchemaBase(BaseSchema):
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthCalculationSchema(NetWorthCalculationSchemaBase):
    Id: UUID


class InNetWorthCalculationSchema(NetWorthCalculationSchemaBase):
    ...


class OutNetWorthCalculationSchema(NetWorthCalculationSchema):
    ...
