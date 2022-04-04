from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.banks import Banks
from app.models.schema.banks import BanksSchemaBase, BanksSchema, InBanksSchema


class BanksRepository(BaseRepository[BanksSchemaBase, BanksSchema, Banks]):
    @property
    def _in_schema(self) -> Type[BanksSchemaBase]:
        return InBanksSchema

    @property
    def _schema(self) -> Type[BanksSchema]:
        return BanksSchema

    @property
    def _table(self) -> Type[Banks]:
        return Banks
