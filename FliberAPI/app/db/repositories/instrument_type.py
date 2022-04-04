from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.instrument_type import InstrumentType
from app.models.schema.instrument_type import (
    InstrumentTypeSchemaBase,
    InstrumentTypeSchema,
    InInstrumentTypeSchema,
)


class InstrumentTypeRepository(
    BaseRepository[InstrumentTypeSchemaBase, InstrumentTypeSchema, InstrumentType]
):
    @property
    def _in_schema(self) -> Type[InstrumentTypeSchemaBase]:
        return InInstrumentTypeSchema

    @property
    def _schema(self) -> Type[InstrumentTypeSchema]:
        return InstrumentTypeSchema

    @property
    def _table(self) -> Type[InstrumentType]:
        return InstrumentType
