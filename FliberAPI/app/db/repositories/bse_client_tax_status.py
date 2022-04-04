from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.bse_client_tax_status import BseClientTaxStatus
from app.models.schema.bse_client_tax_status import (
    BseClientTaxStatusSchemaBase,
    BseClientTaxStatusSchema,
    InBseClientTaxStatusSchema,
)


class BseClientTaxStatusRepository(
    BaseRepository[
        BseClientTaxStatusSchemaBase, BseClientTaxStatusSchema, BseClientTaxStatus
    ]
):
    @property
    def _in_schema(self) -> Type[BseClientTaxStatusSchemaBase]:
        return InBseClientTaxStatusSchema

    @property
    def _schema(self) -> Type[BseClientTaxStatusSchema]:
        return BseClientTaxStatusSchema

    @property
    def _table(self) -> Type[BseClientTaxStatus]:
        return BseClientTaxStatus
