from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class BsePanExemptCategorySchemaBase(BaseSchema):

    Category: int
    Description: str
    CreatedOn: datetime


class BsePanExemptCategorySchema(BsePanExemptCategorySchemaBase):
    Id: UUID


class InBsePanExemptCategorySchema(BsePanExemptCategorySchemaBase):
    ...


class OutBsePanExemptCategorySchema(BsePanExemptCategorySchema):
    ...
