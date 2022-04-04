from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class MaritalStatusSchemaBase(BaseSchema):

    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool


class MaritalStatusSchema(MaritalStatusSchemaBase):
    Id: UUID


class InMaritalStatusSchema(MaritalStatusSchemaBase):
    ...


class OutMaritalStatusSchema(MaritalStatusSchema):
    ...

    