from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class NomineeRelationSchemaBase(BaseSchema):
    Code: int
    Description: str
    CreatedOn: datetime
    IsDeleted: bool = False


class NomineeRelationSchema(NomineeRelationSchemaBase):
    Id: UUID


class InNomineeRelationSchema(NomineeRelationSchemaBase):
    ...


class OutNomineeRelationSchema(NomineeRelationSchema):
    ...
