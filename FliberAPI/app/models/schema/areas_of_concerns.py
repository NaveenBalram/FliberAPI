from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class AreasOfConcernsSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class AreasOfConcernsSchema(AreasOfConcernsSchemaBase):
    Id: UUID


class InAreasOfConcernsSchema(AreasOfConcernsSchemaBase):
    ...


class OutAreasOfConcernsSchema(AreasOfConcernsSchema):
    ...
