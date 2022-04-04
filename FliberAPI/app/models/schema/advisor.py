from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class AdvisorSchemaBase(BaseSchema):
    Name: str
    Description: str
    CreatedOn: datetime
    UpdatedOn: datetime
    Ref_Id: int


class AdvisorSchema(AdvisorSchemaBase):
    Id: UUID


class InAdvisorSchema(AdvisorSchemaBase):
    ...


class OutAdvisorSchema(AdvisorSchema):
    ...
