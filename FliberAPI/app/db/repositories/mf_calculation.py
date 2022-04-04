from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.mf_calculation import MfCalculation
from app.models.schema.mf_calculation import MfCalculationSchemaBase, MfCalculationSchema, MfCalculationSchema, InMfCalculationSchema


class MfCalculationRepository(BaseRepository[MfCalculationSchemaBase, MfCalculationSchema, MfCalculation]):
    @property
    def _in_schema(self) -> Type[MfCalculationSchemaBase]:
        return InMfCalculationSchema

    @property
    def _schema(self) -> Type[MfCalculationSchema]:
        return MfCalculationSchema

    @property
    def _table(self) -> Type[MfCalculation]:
        return MfCalculation
