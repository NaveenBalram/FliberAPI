from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class CasDataUploadToPulseLabSchemaBase(BaseSchema):

    UserId: UUID
    CasFile: str
    Password: str
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool


class CasDataUploadToPulseLabSchema(CasDataUploadToPulseLabSchemaBase):
    Id: UUID


class InCasDataUploadToPulseLabSchema(CasDataUploadToPulseLabSchemaBase):
    ...


class OutCasDataUploadToPulseLabSchema(CasDataUploadToPulseLabSchema):
    ...
