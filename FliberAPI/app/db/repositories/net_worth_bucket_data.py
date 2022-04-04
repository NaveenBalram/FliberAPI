from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_bucket_data import NetWorthBucketData
from app.models.schema.net_worth_bucket_data import NetWorthBucketDataSchemaBase, NetWorthBucketDataSchema, \
    InNetWorthBucketDataSchema


class NetWorthBucketDataRepository(
    BaseRepository[NetWorthBucketDataSchemaBase, NetWorthBucketDataSchema, NetWorthBucketData]):
    @property
    def _in_schema(self) -> Type[NetWorthBucketDataSchemaBase]:
        return InNetWorthBucketDataSchema

    @property
    def _schema(self) -> Type[NetWorthBucketDataSchema]:
        return NetWorthBucketDataSchema

    @property
    def _table(self) -> Type[NetWorthBucketData]:
        return NetWorthBucketData
