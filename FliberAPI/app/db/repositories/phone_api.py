from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.phone_api import PhoneApi
from app.models.schema.phone_api import (
    PhoneApiSchemaBase,
    PhoneApiSchema,
    PhoneApiSchema,
    InPhoneApiSchema,
)


class PhoneApiRepository(BaseRepository[PhoneApiSchemaBase, PhoneApiSchema, PhoneApi]):
    @property
    def _in_schema(self) -> Type[PhoneApiSchemaBase]:
        return InPhoneApiSchema

    @property
    def _schema(self) -> Type[PhoneApiSchema]:
        return PhoneApiSchema

    @property
    def _table(self) -> Type[PhoneApi]:
        return PhoneApi
