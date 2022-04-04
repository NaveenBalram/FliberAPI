from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.investment_type import InvestmentType
from app.models.schema.investment_type import (
    InvestmentTypeSchemaBase,
    InvestmentTypeSchema,
    InInvestmentTypeSchema,
)


class InvestmentTypeRepository(
    BaseRepository[InvestmentTypeSchemaBase, InvestmentTypeSchema, InvestmentType]
):
    @property
    def _in_schema(self) -> Type[InvestmentTypeSchemaBase]:
        return InInvestmentTypeSchema

    @property
    def _schema(self) -> Type[InvestmentTypeSchema]:
        return InvestmentTypeSchema

    @property
    def _table(self) -> Type[InvestmentType]:
        return InvestmentType
