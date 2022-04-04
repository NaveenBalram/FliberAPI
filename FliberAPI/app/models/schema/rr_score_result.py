from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class RrScoreResultSchemaBase(BaseSchema):
    UserId: UUID
    RRScoreResult: str
    CorpusRequired: float
    ExpectedValueOfExistingInvestments: float
    UserAge: int
    RetirementAge: int
    AmountRequired: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool


class RrScoreResultSchema(RrScoreResultSchemaBase):
    Id: UUID


class InRrScoreResultSchema(RrScoreResultSchemaBase):
    ...


class OutRrScoreResultSchema(RrScoreResultSchema):
    ...

