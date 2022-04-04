from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class PolicyWeightageSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class PolicyWeightageSchema(PolicyWeightageSchemaBase):
    Id: UUID


class InPolicyWeightageSchema(PolicyWeightageSchemaBase):
    ...


class OutPolicyWeightageSchema(PolicyWeightageSchema):
    ...
