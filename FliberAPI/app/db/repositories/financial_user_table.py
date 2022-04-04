from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.financial_user_table import FinancialUserTable
from app.models.schema.financial_user_table import FinancialUserTableSchemaBase, \
    FinancialUserTableSchema, InFinancialUserTableSchema


class FinancialUserTableRepository(
    BaseRepository[FinancialUserTableSchemaBase, FinancialUserTableSchema, FinancialUserTable]):
    @property
    def _in_schema(self) -> Type[FinancialUserTableSchemaBase]:
        return InFinancialUserTableSchema

    @property
    def _schema(self) -> Type[FinancialUserTableSchema]:
        return FinancialUserTableSchema

    @property
    def _table(self) -> Type[FinancialUserTable]:
        return FinancialUserTable
