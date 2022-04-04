from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.ppf_calculation import PpfCalculation
from app.models.schema.ppf_calculation import PpfCalculationSchemaBase, PpfCalculationSchema, PpfCalculationSchema, InPpfCalculationSchema


class PpfCalculationRepository(BaseRepository[PpfCalculationSchemaBase, PpfCalculationSchema, PpfCalculation]):
    @property
    def _in_schema(self) -> Type[PpfCalculationSchemaBase]:
        return InPpfCalculationSchema

    @property
    def _schema(self) -> Type[PpfCalculationSchema]:
        return PpfCalculationSchema

    @property
    def _table(self) -> Type[PpfCalculation]:
        return PpfCalculation
