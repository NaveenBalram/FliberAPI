from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.bse_income_slab import BSEIncomeSlab
from app.models.schema.bse_income_slab import (
    BSEIncomeSlabSchemaBase,
    BSEIncomeSlabSchema,
    InBSEIncomeSlabSchema,
)


class BSEIncomeSlabRepository(
    BaseRepository[BSEIncomeSlabSchemaBase, BSEIncomeSlabSchema, BSEIncomeSlab]
):
    @property
    def _in_schema(self) -> Type[BSEIncomeSlabSchemaBase]:
        return InBSEIncomeSlabSchema

    @property
    def _schema(self) -> Type[BSEIncomeSlabSchema]:
        return BSEIncomeSlabSchema

    @property
    def _table(self) -> Type[BSEIncomeSlab]:
        return BSEIncomeSlab
