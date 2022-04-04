from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.investment_bucket import InvestmentBucket
from app.models.schema.investment_bucket import (
    InvestmentBucketSchemaBase,
    InvestmentBucketSchema,
    InInvestmentBucketSchema,
)


class InvestmentBucketRepository(
    BaseRepository[InvestmentBucketSchemaBase, InvestmentBucketSchema, InvestmentBucket]
):
    @property
    def _in_schema(self) -> Type[InvestmentBucketSchemaBase]:
        return InInvestmentBucketSchema

    @property
    def _schema(self) -> Type[InvestmentBucketSchema]:
        return InvestmentBucketSchema

    @property
    def _table(self) -> Type[InvestmentBucket]:
        return InvestmentBucket
