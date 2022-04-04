from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class BseCountryCodeSchemaBase(BaseSchema):

    Code: int
    CountryName: str
    CreatedOn: datetime


class BseCountryCodeSchema(BseCountryCodeSchemaBase):
    Id: UUID


class InBseCountryCodeSchema(BseCountryCodeSchemaBase):
    ...


class OutBseCountryCodeSchema(BseCountryCodeSchema):
    ...
