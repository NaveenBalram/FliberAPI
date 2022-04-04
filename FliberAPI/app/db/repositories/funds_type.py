from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.funds_type import FundsType
from app.models.schema.funds_type import (
    FundsTypeSchemaBase,
    FundsTypeSchema,
    InFundsTypeSchema,
)


class FundsTypeRepository(
    BaseRepository[FundsTypeSchemaBase, FundsTypeSchema, FundsType]
):
    @property
    def _in_schema(self) -> Type[FundsTypeSchemaBase]:
        return InFundsTypeSchema

    @property
    def _schema(self) -> Type[FundsTypeSchema]:
        return FundsTypeSchema

    @property
    def _table(self) -> Type[FundsType]:
        return FundsType
