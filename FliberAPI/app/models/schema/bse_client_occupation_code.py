from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class BseClientOccupationCodeSchemaBase(BaseSchema):

    Code: int
    Details: str
    CreatedOn: datetime


class BseClientOccupationCodeSchema(BseClientOccupationCodeSchemaBase):
    Id: UUID


class InBseClientOccupationCodeSchema(BseClientOccupationCodeSchemaBase):
    ...


class OutBseClientOccupationCodeSchema(BseClientOccupationCodeSchema):
    ...
