from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.bonds_calculation import BondsCalculation
from app.models.schema.bonds_calculation import BondsCalculationSchemaBase, BondsCalculationSchema, BondsCalculationSchema, InBondsCalculationSchema


class BondsCalculationRepository(BaseRepository[BondsCalculationSchemaBase, BondsCalculationSchema, BondsCalculation]):
    @property
    def _in_schema(self) -> Type[BondsCalculationSchemaBase]:
        return InBondsCalculationSchema

    @property
    def _schema(self) -> Type[BondsCalculationSchema]:
        return BondsCalculationSchema

    @property
    def _table(self) -> Type[BondsCalculation]:
        return BondsCalculation
