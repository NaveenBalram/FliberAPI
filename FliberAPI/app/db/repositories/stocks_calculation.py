from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.stocks_calculation import StocksCalculation
from app.models.schema.stocks_calculation import StocksCalculationSchemaBase, StocksCalculationSchema, StocksCalculationSchema, InStocksCalculationSchema


class StocksCalculationRepository(BaseRepository[StocksCalculationSchemaBase, StocksCalculationSchema, StocksCalculation]):
    @property
    def _in_schema(self) -> Type[StocksCalculationSchemaBase]:
        return InStocksCalculationSchema

    @property
    def _schema(self) -> Type[StocksCalculationSchema]:
        return StocksCalculationSchema

    @property
    def _table(self) -> Type[StocksCalculation]:
        return StocksCalculation
