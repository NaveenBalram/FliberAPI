from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.bse_state_code import BseStateCode
from app.models.schema.bse_state_code import (
    BseStateCodeSchemaBase,
    BseStateCodeSchema,
    InBseStateCodeSchema,
)


class BseStateCodeRepository(
    BaseRepository[BseStateCodeSchemaBase, BseStateCodeSchema, BseStateCode]
):
    @property
    def _in_schema(self) -> Type[BseStateCodeSchemaBase]:
        return InBseStateCodeSchema

    @property
    def _schema(self) -> Type[BseStateCodeSchema]:
        return BseStateCodeSchema

    @property
    def _table(self) -> Type[BseStateCode]:
        return BseStateCode
