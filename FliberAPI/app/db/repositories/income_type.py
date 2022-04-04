from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.income_type import IncomeType
from app.models.schema.income_type import (
    IncomeTypeSchemaBase,
    IncomeTypeSchema,
    InIncomeTypeSchema,
)


class IncomeTypeRepository(
    BaseRepository[IncomeTypeSchemaBase, IncomeTypeSchema, IncomeType]
):
    @property
    def _in_schema(self) -> Type[IncomeTypeSchemaBase]:
        return InIncomeTypeSchema

    @property
    def _schema(self) -> Type[IncomeTypeSchema]:
        return IncomeTypeSchema

    @property
    def _table(self) -> Type[IncomeType]:
        return IncomeType
