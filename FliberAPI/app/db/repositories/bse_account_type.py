from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.bse_account_type import BseAccountType
from app.models.schema.bse_account_type import (
    BseAccountTypeSchemaBase,
    BseAccountTypeSchema,
    InBseAccountTypeSchema,
)


class BseAccountTypeRepository(
    BaseRepository[BseAccountTypeSchemaBase, BseAccountTypeSchema, BseAccountType]
):
    @property
    def _in_schema(self) -> Type[BseAccountTypeSchemaBase]:
        return InBseAccountTypeSchema

    @property
    def _schema(self) -> Type[BseAccountTypeSchema]:
        return BseAccountTypeSchema

    @property
    def _table(self) -> Type[BseAccountType]:
        return BseAccountType
