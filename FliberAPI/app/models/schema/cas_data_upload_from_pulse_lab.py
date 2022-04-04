from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.models.schema.base import BaseSchema


class CasDataUploadFromPulseLabSchemaBase(BaseSchema):
    UserId: UUID
    ClientId: int
    SchemeFolioNo: str
    SchemeName: str
    SchemeCode: str
    UnitBalance: str
    CurrentValue: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool


class CasDataUploadFromPulseLabSchema(CasDataUploadFromPulseLabSchemaBase):
    Id: UUID


class InCasDataUploadFromPulseLabSchema(CasDataUploadFromPulseLabSchemaBase):
    ...


class OutCasDataUploadFromPulseLabSchema(CasDataUploadFromPulseLabSchema):
    ...


class CasData(BaseModel):
    UserId: UUID
    AdvisorId: str
    ClientId: str
    SubAdvisorId: str
