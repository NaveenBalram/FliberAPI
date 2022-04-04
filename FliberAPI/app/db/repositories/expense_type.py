from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.expense_type import ExpenseType
from app.models.schema.expense_type import (
    ExpenseTypeSchemaBase,
    ExpenseTypeSchema,
    InExpenseTypeSchema,
)


class ExpenseTypeRepository(
    BaseRepository[ExpenseTypeSchemaBase, ExpenseTypeSchema, ExpenseType]
):
    @property
    def _in_schema(self) -> Type[ExpenseTypeSchemaBase]:
        return InExpenseTypeSchema

    @property
    def _schema(self) -> Type[ExpenseTypeSchema]:
        return ExpenseTypeSchema

    @property
    def _table(self) -> Type[ExpenseType]:
        return ExpenseType
