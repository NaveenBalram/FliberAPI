from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.cash_free_configuration import CashFreeConfiguration
from app.models.schema.cash_free_configuration import (
    CashFreeConfigurationSchemaBase,
    CashFreeConfigurationSchema,
    CashFreeConfigurationSchema,
)


class CashFreeConfigurationRepository(
    BaseRepository[
        CashFreeConfigurationSchemaBase,
        CashFreeConfigurationSchema,
        CashFreeConfiguration,
    ]
):
    @property
    def _in_schema(self) -> Type[CashFreeConfigurationSchemaBase]:
        return InCashFreeConfigurationSchema

    @property
    def _schema(self) -> Type[CashFreeConfigurationSchema]:
        return CashFreeConfigurationSchema

    @property
    def _table(self) -> Type[CashFreeConfiguration]:
        return CashFreeConfiguration
