from uuid import UUID
from datetime import datetime

from app.models.schema.base import BaseSchema


class BseClientNomineeSchemaBase(BaseSchema):

    UserId: UUID
    NomineeNumber: int
    NomineeName: str
    NomineeRelationship: str
    NomineeApplicablePercent: float
    NomineeMinorFlag: bool = False
    NomineeDOB: datetime
    NomineeGuardian: str
    CreatedOn: datetime


class BseClientNomineeSchema(BseClientNomineeSchemaBase):
    Id: UUID


class InBseClientNomineeSchema(BseClientNomineeSchemaBase):
    ...


class OutBseClientNomineeSchema(BseClientNomineeSchema):
    ...
