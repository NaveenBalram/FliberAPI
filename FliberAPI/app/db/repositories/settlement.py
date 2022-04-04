from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.settlement import Settlement
from app.models.schema.settlement import (
    SettlementSchemaBase,
    SettlementSchema,
    InSettlementSchema,
)


class SettlementRepository(
    BaseRepository[SettlementSchemaBase, SettlementSchema, Settlement]
):
    @property
    def _in_schema(self) -> Type[SettlementSchemaBase]:
        return InSettlementSchema

    @property
    def _schema(self) -> Type[SettlementSchema]:
        return SettlementSchema

    @property
    def _table(self) -> Type[Settlement]:
        return Settlement
