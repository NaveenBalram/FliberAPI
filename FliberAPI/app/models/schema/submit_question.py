from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class SubmitQuestionSchemaBase(BaseSchema):
    QuestionId: UUID
    UserId: UUID
    ChoiceId: str
    UserText: str
    SelectedValue: int
    ModuleType: int
    ChoiceSequence: int
    CreatedOn: datetime
    UpdatedOn: datetime


class SubmitQuestionSchema(SubmitQuestionSchemaBase):
    Id: UUID


class InSubmitQuestionSchema(SubmitQuestionSchemaBase):
    ...


class OutSubmitQuestionSchema(SubmitQuestionSchema):
    ...
