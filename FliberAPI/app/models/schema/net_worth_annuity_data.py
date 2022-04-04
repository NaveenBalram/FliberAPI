from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class NetWorthAnnuityDataSchemaBase(BaseSchema):
    UserId: UUID
    CategoryId: UUID
    BucketId: UUID
    SchemeName: str
    AccountNumber: str
    StartDate: datetime
    SchemeType: UUID
    Corpus: float
    AnnuityIncome: float
    Frequency: UUID
    GrowthOfPension: float
    AnnuityMaturity: datetime
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthAnnuityDataSchema(NetWorthAnnuityDataSchemaBase):
    Id: UUID


class InNetWorthAnnuityDataSchema(NetWorthAnnuityDataSchemaBase):
    ...


class OutNetWorthAnnuityDataSchema(NetWorthAnnuityDataSchema):
    ...

