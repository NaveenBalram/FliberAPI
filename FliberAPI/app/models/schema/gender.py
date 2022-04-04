from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class GenderSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime = datetime.now()
    UpdatedOn: datetime = datetime.now()
    Ref_Id: int


class GenderSchema(GenderSchemaBase):
    Id: UUID


class InGenderSchema(GenderSchemaBase):
    ...


class OutGenderSchema(GenderSchema):
    ...
