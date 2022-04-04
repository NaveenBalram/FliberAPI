from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class ChoiceSchemaBase(BaseSchema):
    Text: str
    Description: str
    Value: int
    ChoiceSequence: int
    QuestionId: UUID
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime
    Ref_Id: int


class ChoiceSchema(ChoiceSchemaBase):
    Id: UUID


class InChoiceSchema(ChoiceSchemaBase):
    ...


class OutChoiceSchema(ChoiceSchema):
    ...
