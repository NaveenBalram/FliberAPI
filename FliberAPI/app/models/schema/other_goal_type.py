from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class OtherGoalTypeSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class OtherGoalTypeSchema(OtherGoalTypeSchemaBase):
    Id: UUID


class InOtherGoalTypeSchema(OtherGoalTypeSchemaBase):
    ...


class OutOtherGoalTypeSchema(OtherGoalTypeSchema):
    ...
