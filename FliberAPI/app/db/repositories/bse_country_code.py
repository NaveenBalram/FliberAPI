from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.bse_country_code import BseCountryCode
from app.models.schema.bse_country_code import (
    BseCountryCodeSchemaBase,
    BseCountryCodeSchema,
    InBseCountryCodeSchema,
)


class BseCountryCodeRepository(
    BaseRepository[BseCountryCodeSchemaBase, BseCountryCodeSchema, BseCountryCode]
):
    @property
    def _in_schema(self) -> Type[BseCountryCodeSchemaBase]:
        return InBseCountryCodeSchema

    @property
    def _schema(self) -> Type[BseCountryCodeSchema]:
        return BseCountryCodeSchema

    @property
    def _table(self) -> Type[BseCountryCode]:
        return BseCountryCode
