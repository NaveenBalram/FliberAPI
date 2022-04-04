from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.income import Income
from app.models.schema.income import IncomeSchemaBase, IncomeSchema, InIncomeSchema


class IncomeRepository(BaseRepository[IncomeSchemaBase, IncomeSchema, Income]):
    @property
    def _in_schema(self) -> Type[IncomeSchemaBase]:
        return InIncomeSchema

    @property
    def _schema(self) -> Type[IncomeSchema]:
        return IncomeSchema

    @property
    def _table(self) -> Type[Income]:
        return Income
