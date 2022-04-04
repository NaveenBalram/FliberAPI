from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class OccupationTypesSchemaBase(BaseSchema):

    Code: int
    Description: str
    CreatedOn: datetime


class OccupationTypesSchema(OccupationTypesSchemaBase):
    Id: UUID


class InOccupationTypesSchema(OccupationTypesSchemaBase):
    ...


class OutOccupationTypesSchema(OccupationTypesSchema):
    ...
