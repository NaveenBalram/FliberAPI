from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.rule_asset_allocation import RuleAssetAllocation
from app.models.schema.rule_asset_allocation import RuleAssetAllocationSchema, RuleAssetAllocationSchemaBase


class RuleAssetAllocationRepository(
    BaseRepository[RuleAssetAllocationSchema, RuleAssetAllocationSchemaBase, RuleAssetAllocation]):
    @property
    def _in_schema(self) -> Type[RuleAssetAllocationSchema]:
        return RuleAssetAllocationSchema

    @property
    def _schema(self) -> Type[RuleAssetAllocationSchemaBase]:
        return RuleAssetAllocationSchemaBase

    @property
    def _table(self) -> Type[RuleAssetAllocation]:
        return RuleAssetAllocation
