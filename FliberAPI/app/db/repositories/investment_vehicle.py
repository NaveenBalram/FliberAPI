from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.investment_vehicle import InvestmentVehicle
from app.models.schema.investment_vehicle import (
    InvestmentVehicleSchemaBase,
    InvestmentVehicleSchema,
    InInvestmentVehicleSchema,
)


class InvestmentVehicleRepository(
    BaseRepository[
        InvestmentVehicleSchemaBase, InvestmentVehicleSchema, InvestmentVehicle
    ]
):
    @property
    def _in_schema(self) -> Type[InvestmentVehicleSchemaBase]:
        return InInvestmentVehicleSchema

    @property
    def _schema(self) -> Type[InvestmentVehicleSchema]:
        return InvestmentVehicleSchema

    @property
    def _table(self) -> Type[InvestmentVehicle]:
        return InvestmentVehicle
