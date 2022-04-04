from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class CorpusStatusSchemaBase(BaseSchema):
    Name: str
    Description: str
    LowRange: int
    HighRange: int
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime
    Ref_id: int


class CorpusStatusSchema(CorpusStatusSchemaBase):
    Id: UUID


class InCorpusStatusSchema(CorpusStatusSchemaBase):
    ...


class OutCorpusStatusSchema(CorpusStatusSchema):
    ...
