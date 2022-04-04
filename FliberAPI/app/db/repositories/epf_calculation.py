from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.epf_calculation import EpfCalculation
from app.models.schema.epf_calculation import EpfCalculationSchemaBase, EpfCalculationSchema, EpfCalculationSchema, InEpfCalculationSchema


class EpfCalculationRepository(BaseRepository[EpfCalculationSchemaBase, EpfCalculationSchema, EpfCalculation]):
    @property
    def _in_schema(self) -> Type[EpfCalculationSchemaBase]:
        return InEpfCalculationSchema

    @property
    def _schema(self) -> Type[EpfCalculationSchema]:
        return EpfCalculationSchema

    @property
    def _table(self) -> Type[EpfCalculation]:
        return EpfCalculation
