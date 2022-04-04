from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class QuestionSchemaBase(BaseSchema):
    QuestionTitle: str
    Description: str
    PreviousQuestionId: int
    QuestionTypeId: UUID
    AdvisorId: UUID
    QuestionSequence: int
    CreatedOn: datetime
    UpdatedOn: datetime
    Ref_Id: int


class QuestionSchema(QuestionSchemaBase):
    Id: UUID


class InQuestionSchema(QuestionSchemaBase):
    ...


class OutQuestionSchema(QuestionSchema):
    ...
