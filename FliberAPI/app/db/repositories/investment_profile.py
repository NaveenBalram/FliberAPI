from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.investment_profile import InvestmentProfile
from app.models.schema.investment_profile import (
    InvestmentProfileSchemaBase,
    InvestmentProfileSchema,
    InInvestmentProfileSchema,
)


class InvestmentProfileRepository(
    BaseRepository[
        InvestmentProfileSchemaBase, InvestmentProfileSchema, InvestmentProfile
    ]
):
    @property
    def _in_schema(self) -> Type[InvestmentProfileSchemaBase]:
        return InInvestmentProfileSchema

    @property
    def _schema(self) -> Type[InvestmentProfileSchema]:
        return InvestmentProfileSchema

    @property
    def _table(self) -> Type[InvestmentProfile]:
        return InvestmentProfile
