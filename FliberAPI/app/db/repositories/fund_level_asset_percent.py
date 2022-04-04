from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.fund_level_asset_percent import FundLevelAssetPercent
from app.models.schema.fund_level_asset_percent import (
    FundLevelAssetPercentSchemaBase,
    FundLevelAssetPercentSchema,
    FundLevelAssetPercentSchema,
    InFundLevelAssetPercentSchema,
)


class FundLevelAssetPercentRepository(
    BaseRepository[
        FundLevelAssetPercentSchemaBase,
        FundLevelAssetPercentSchema,
        FundLevelAssetPercent,
    ]
):
    @property
    def _in_schema(self) -> Type[FundLevelAssetPercentSchemaBase]:
        return InFundLevelAssetPercentSchema

    @property
    def _schema(self) -> Type[FundLevelAssetPercentSchema]:
        return FundLevelAssetPercentSchema

    @property
    def _table(self) -> Type[FundLevelAssetPercent]:
        return FundLevelAssetPercent
