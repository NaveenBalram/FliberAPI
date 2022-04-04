from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class CasUploadSchemaBase(BaseSchema):

    Name: str
    Category: str
    SubCategory: bool
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool


class CasUploadSchema(CasUploadSchemaBase):
    Id: UUID


class InCasUploadSchema(CasUploadSchemaBase):
    ...


class OutCasUploadSchema(CasUploadSchema):
    ...

    