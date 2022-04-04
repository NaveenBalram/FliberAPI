from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.asset_allocation_attributes import AssetAllocationAttributes
from app.models.schema.asset_allocation_attributes import (
    AssetAllocationAttributesSchemaBase,
    AssetAllocationAttributesSchema,
    InAssetAllocationAttributesSchema,
)


class AssetAllocationAttributesRepository(
    BaseRepository[
        AssetAllocationAttributesSchemaBase,
        AssetAllocationAttributesSchema,
        AssetAllocationAttributes,
    ]
):
    @property
    def _in_schema(self) -> Type[AssetAllocationAttributesSchemaBase]:
        return InAssetAllocationAttributesSchema

    @property
    def _schema(self) -> Type[AssetAllocationAttributesSchema]:
        return AssetAllocationAttributesSchema

    @property
    def _table(self) -> Type[AssetAllocationAttributes]:
        return AssetAllocationAttributes
