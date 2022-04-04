from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.bank_branches import BankBranches
from app.models.schema.bank_branches import (
    BankBranchesSchemaBase,
    BankBranchesSchema,
    InBankBranchesSchema,
)


class BankBranchesRepository(
    BaseRepository[BankBranchesSchemaBase, BankBranchesSchema, BankBranches]
):
    @property
    def _in_schema(self) -> Type[BankBranchesSchemaBase]:
        return InBankBranchesSchema

    @property
    def _schema(self) -> Type[BankBranchesSchema]:
        return BankBranchesSchema

    @property
    def _table(self) -> Type[BankBranches]:
        return BankBranches
