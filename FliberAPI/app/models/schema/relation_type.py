from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class RelationTypeSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class RelationTypeSchema(RelationTypeSchemaBase):
    Id: UUID


class InRelationTypeSchema(RelationTypeSchemaBase):
    ...


class OutRelationTypeSchema(RelationTypeSchema):
    ...
