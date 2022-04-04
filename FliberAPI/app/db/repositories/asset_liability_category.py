from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.asset_liability_category import AssetLiabilityCategory
from app.models.schema.asset_liability_category import (
    AssetLiabilityCategorySchemaBase,
    AssetLiabilityCategorySchema,
    InAssetLiabilityCategorySchema,
)


class AssetLiabilityCategoryRepository(
    BaseRepository[
        AssetLiabilityCategorySchemaBase,
        AssetLiabilityCategorySchema,
        AssetLiabilityCategory,
    ]
):
    @property
    def _in_schema(self) -> Type[AssetLiabilityCategorySchemaBase]:
        return InAssetLiabilityCategorySchema

    @property
    def _schema(self) -> Type[AssetLiabilityCategorySchema]:
        return AssetLiabilityCategorySchema

    @property
    def _table(self) -> Type[AssetLiabilityCategory]:
        return AssetLiabilityCategory
