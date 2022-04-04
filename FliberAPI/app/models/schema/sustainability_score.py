from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class SustainabilityScoreSchemaBase(BaseSchema):

    Mobile: str
    Password: str
    IsMobileVerified: bool
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool


class SustainabilityScoreSchema(SustainabilityScoreSchemaBase):
    Id: UUID


class InSustainabilityScoreSchema(SustainabilityScoreSchemaBase):
    ...


class OutSustainabilityScoreSchema(SustainabilityScoreSchema):
    ...

