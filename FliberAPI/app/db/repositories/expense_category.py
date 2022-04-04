from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.expense_category import ExpenseCategory
from app.models.schema.expense_category import (
    ExpenseCategorySchemaBase,
    ExpenseCategorySchema,
    InExpenseCategorySchema,
)


class ExpenseCategoryRepository(
    BaseRepository[ExpenseCategorySchemaBase, ExpenseCategorySchema, ExpenseCategory]
):
    @property
    def _in_schema(self) -> Type[ExpenseCategorySchemaBase]:
        return InExpenseCategorySchema

    @property
    def _schema(self) -> Type[ExpenseCategorySchema]:
        return ExpenseCategorySchema

    @property
    def _table(self) -> Type[ExpenseCategory]:
        return ExpenseCategory
