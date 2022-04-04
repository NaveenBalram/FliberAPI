from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class QuestionTypeSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime
    Ref_Id: int


class QuestionTypeSchema(QuestionTypeSchemaBase):
    Id: UUID


class InQuestionTypeSchema(QuestionTypeSchemaBase):
    ...


class OutQuestionTypeSchema(QuestionTypeSchema):
    ...
