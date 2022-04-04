from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class PhoneApiSchemaBase(BaseSchema):

    Phone: str
    Password: str
    IsMobileVerified: bool
    IsResidentialInformation: bool
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class PhoneApiSchema(PhoneApiSchemaBase):
    Id: UUID


class InPhoneApiSchema(PhoneApiSchemaBase):
    ...


class OutPhoneApiSchema(PhoneApiSchema):
    ...
