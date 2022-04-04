from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.bank_account_type import BankAccountType
from app.models.schema.bank_account_type import (
    BankAccountTypeSchemaBase,
    BankAccountTypeSchema,
    InBankAccountTypeSchema,
)


class BankAccountTypeRepository(
    BaseRepository[BankAccountTypeSchemaBase, BankAccountTypeSchema, BankAccountType]
):
    @property
    def _in_schema(self) -> Type[BankAccountTypeSchemaBase]:
        return InBankAccountTypeSchema

    @property
    def _schema(self) -> Type[BankAccountTypeSchema]:
        return BankAccountTypeSchema

    @property
    def _table(self) -> Type[BankAccountType]:
        return BankAccountType
