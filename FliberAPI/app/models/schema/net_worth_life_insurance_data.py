from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class NetWorthLifeInsuranceDataSchemaBase(BaseSchema):
    UserId: UUID
    CategoryId: UUID
    BucketId: UUID
    PolicyProvider: str
    SchemaName: str
    PolicyNumber: str
    PolicyType: str
    StartDate: datetime
    PolicyTerm: str
    SumAssured: float
    MaturityValue: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthLifeInsuranceDataSchema(NetWorthLifeInsuranceDataSchemaBase):
    Id: UUID


class InNetWorthLifeInsuranceDataSchema(NetWorthLifeInsuranceDataSchemaBase):
    ...


class OutNetWorthLifeInsuranceDataSchema(NetWorthLifeInsuranceDataSchema):
    ...
