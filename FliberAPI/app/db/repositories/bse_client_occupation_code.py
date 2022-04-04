from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.bse_client_occupation_code import BseClientOccupationCode
from app.models.schema.bse_client_occupation_code import (
    BseClientOccupationCodeSchemaBase,
    BseClientOccupationCodeSchema,
    InBseClientOccupationCodeSchema,
)


class BseClientOccupationCodeRepository(
    BaseRepository[
        BseClientOccupationCodeSchemaBase,
        BseClientOccupationCodeSchema,
        BseClientOccupationCode,
    ]
):
    @property
    def _in_schema(self) -> Type[BseClientOccupationCodeSchemaBase]:
        return InBseClientOccupationCodeSchema

    @property
    def _schema(self) -> Type[BseClientOccupationCodeSchema]:
        return BseClientOccupationCodeSchema

    @property
    def _table(self) -> Type[BseClientOccupationCode]:
        return BseClientOccupationCode
