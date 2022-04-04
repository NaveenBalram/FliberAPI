from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.others_calculation import OthersCalculation
from app.models.schema.others_calculation import OthersCalculationSchemaBase, OthersCalculationSchema, OthersCalculationSchema, InOthersCalculationSchema


class OthersCalculationRepository(BaseRepository[OthersCalculationSchemaBase, OthersCalculationSchema, OthersCalculation]):
    @property
    def _in_schema(self) -> Type[OthersCalculationSchemaBase]:
        return InOthersCalculationSchema

    @property
    def _schema(self) -> Type[OthersCalculationSchema]:
        return OthersCalculationSchema

    @property
    def _table(self) -> Type[OthersCalculation]:
        return OthersCalculation
