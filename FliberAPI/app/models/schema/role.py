from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class RoleSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class RoleSchema(RoleSchemaBase):
    Id: UUID


class InRoleSchema(RoleSchemaBase):
    ...


class OutRoleSchema(RoleSchema):
    ...
