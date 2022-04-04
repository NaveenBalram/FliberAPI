from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class EpfoAutoFetchSchemaBase(BaseSchema):

    Name: str
    Category: str
    SubCategory: bool
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool


class EpfoAutoFetchSchema(EpfoAutoFetchSchemaBase):
    Id: UUID


class InEpfoAutoFetchSchema(EpfoAutoFetchSchemaBase):
    ...


class OutEpfoAutoFetchSchema(EpfoAutoFetchSchema):
    ...

    