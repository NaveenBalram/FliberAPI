from uuid import UUID
from datetime import datetime

from app.models.schema.base import BaseSchema


class NetWorthLoanTypeDataSchemaBase(BaseSchema):
    Name: str
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthLoanTypeDataSchema(NetWorthLoanTypeDataSchemaBase):
    Id: UUID


class InNetWorthLoanTypeDataSchema(NetWorthLoanTypeDataSchemaBase):
    ...


class OutNetWorthLoanTypeDataSchema(NetWorthLoanTypeDataSchema):
    ...
