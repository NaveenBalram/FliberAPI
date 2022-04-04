from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class UserAnswersSchemaBase(BaseSchema):
    UserId: UUID
    QuestionId: str
    SubQuestionId: UUID
    UserAnswer: int
    CreatedOn: datetime
    UpdatedOn: datetime


class UserAnswersSchema(UserAnswersSchemaBase):
    Id: UUID


class InUserAnswersSchema(UserAnswersSchemaBase):
    ...


class OutUserAnswersSchema(UserAnswersSchema):
    ...
