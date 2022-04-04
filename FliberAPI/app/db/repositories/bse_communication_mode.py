from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.bse_communication_mode import BseCommunicationMode
from app.models.schema.bse_communication_mode import (
    BseCommunicationModeSchemaBase,
    BseCommunicationModeSchema,
    InBseCommunicationModeSchema,
)


class BseCommunicationModeRepository(
    BaseRepository[
        BseCommunicationModeSchemaBase, BseCommunicationModeSchema, BseCommunicationMode
    ]
):
    @property
    def _in_schema(self) -> Type[BseCommunicationModeSchemaBase]:
        return InBseCommunicationModeSchema

    @property
    def _schema(self) -> Type[BseCommunicationModeSchema]:
        return BseCommunicationModeSchema

    @property
    def _table(self) -> Type[BseCommunicationMode]:
        return BseCommunicationMode
