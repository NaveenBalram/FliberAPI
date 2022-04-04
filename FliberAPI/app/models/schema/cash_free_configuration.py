from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class CashFreeConfigurationSchemaBase(BaseSchema):

    KeyId: str
    KeySecret: str
    CreatedOn: datetime
    UpdatedOn: datetime


class CashFreeConfigurationSchema(CashFreeConfigurationSchemaBase):
    Id: UUID


class InCashFreeConfigurationSchema(CashFreeConfigurationSchemaBase):
    ...


class OutCashFreeConfigurationSchema(CashFreeConfigurationSchema):
    ...
