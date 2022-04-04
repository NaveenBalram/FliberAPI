from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.nps_calculation import NpsCalculation
from app.models.schema.nps_calculation import NpsCalculationSchemaBase, NpsCalculationSchema, NpsCalculationSchema, InNpsCalculationSchema


class NpsCalculationRepository(BaseRepository[NpsCalculationSchemaBase, NpsCalculationSchema, NpsCalculation]):
    @property
    def _in_schema(self) -> Type[NpsCalculationSchemaBase]:
        return InNpsCalculationSchema

    @property
    def _schema(self) -> Type[NpsCalculationSchema]:
        return NpsCalculationSchema

    @property
    def _table(self) -> Type[NpsCalculation]:
        return NpsCalculation
