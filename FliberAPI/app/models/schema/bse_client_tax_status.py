from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class BseClientTaxStatusSchemaBase(BaseSchema):

    Code: int
    TaxStatus: str
    CreatedOn: datetime


class BseClientTaxStatusSchema(BseClientTaxStatusSchemaBase):
    Id: UUID


class InBseClientTaxStatusSchema(BseClientTaxStatusSchemaBase):
    ...


class OutBseClientTaxStatusSchema(BseClientTaxStatusSchema):
    ...
