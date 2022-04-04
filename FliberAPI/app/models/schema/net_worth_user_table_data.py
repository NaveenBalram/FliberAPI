from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class NetWorthUserTableDataSchemaBase(BaseSchema):
    UserId: UUID
    CategoryId: UUID
    BucketId: UUID
    Description: str
    PropertyLocation: str
    SopLop: str
    RegistrationYear: datetime
    TodaysValue: float
    PlannedForLiquidityFlag: bool
    TargetLiquidityYear: datetime
    ExpectedPrice: float
    VehicleType: UUID
    EstimatedValue: float
    AssetName: str
    AccountNumber: float
    CurrentBalance: float
    FdStartDate: datetime
    MaturityDate: datetime
    PrincipalAmount: float
    MaturityAmount: float
    SchemeName: str
    PolicyNumber: str
    PolicyType: str
    PolicyTerm: str
    SumAssured: float
    MaturityValue: float
    LoanType: UUID
    Lender: str
    OutStandingAmount: float
    SchemeType: UUID
    Corpus: float
    AnnuityIncome: float
    FrequencyId: UUID
    GrowthOfPension: float
    AnnuityMaturity: datetime
    PensionAmount: float
    GrowthAmount: float
    Property: str
    RentalInformation: str
    YearlyAmount: float
    Instrument: str
    InterestPerYearOrDividend: float
    TargetDate: datetime
    Amount: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthUserTableDataSchema(NetWorthUserTableDataSchemaBase):
    Id: UUID


class InNetWorthUserTableDataSchema(NetWorthUserTableDataSchemaBase):
    ...


class OutNetWorthUserTableDataSchema(NetWorthUserTableDataSchema):
    ...
