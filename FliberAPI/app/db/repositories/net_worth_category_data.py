from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_category_data import NetWorthCategoryData
from app.models.schema.net_worth_category_data import NetWorthCategoryDataSchemaBase, NetWorthCategoryDataSchema, \
    InNetWorthCategoryDataSchema


class NetWorthCategoryDataRepository(
    BaseRepository[NetWorthCategoryDataSchemaBase, NetWorthCategoryDataSchema, NetWorthCategoryData]):
    @property
    def _in_schema(self) -> Type[NetWorthCategoryDataSchemaBase]:
        return InNetWorthCategoryDataSchema

    @property
    def _schema(self) -> Type[NetWorthCategoryDataSchema]:
        return NetWorthCategoryDataSchema

    @property
    def _table(self) -> Type[NetWorthCategoryData]:
        return NetWorthCategoryData
