import uuid
from datetime import datetime
from typing import Type
from app.db.errors import DoesNotExist

from sqlalchemy import insert, update, select
from app.db.repositories.base import BaseRepository
from app.db.tables.rule_asset_allocation import RuleAssetAllocation
from app.db.tables.rule_condition import RuleCondition
from app.db.tables.universe_table import UniverseTable
from app.db.tables.asset_class_hierarchy import AssetClassHierarchy
from app.models.schema.rule_condition import (
    RuleConditionSchema,
    RuleConditionSchemaBase,
    InRuleConditionSchema,
)
from itertools import groupby
from operator import attrgetter


class AssetAdvaisoryRepository(
    BaseRepository[RuleConditionSchemaBase, RuleCondition, RuleCondition]
):
    @property
    def _in_schema(self) -> Type[RuleConditionSchemaBase]:
        return RuleConditionSchemaBase

    @property
    def _schema(self) -> Type[RuleConditionSchema]:
        return RuleConditionSchemaBase

    @property
    def _table(self) -> Type[RuleCondition]:
        return RuleCondition

    async def get_all_data(self, risk_category, funding, time_to_retirement):

        result = await self._db_session.execute(
            select(self._table.Id, RuleAssetAllocation.AllocationPercentage, RuleAssetAllocation.assetType,
                UniverseTable.legalname,
                UniverseTable.fundame, UniverseTable.fundlevelcategoryname, AssetClassHierarchy.assetClass).
                join(RuleAssetAllocation).
                outerjoin(UniverseTable, UniverseTable.fundlevelcategoryname == RuleAssetAllocation.assetType).
                outerjoin(AssetClassHierarchy, AssetClassHierarchy.assetType == RuleAssetAllocation.assetType).
                where(
                self._table.RiskCategory == risk_category).
                where(
                self._table.Id == RuleAssetAllocation.RuleId).
                filter(self._table.FundingMinAmount < funding).
                filter(self._table.FundingMaxAmount >= funding).
                filter(self._table.TimetoRetirementMin < time_to_retirement).
                filter(self._table.TimetoRetirementMax >= time_to_retirement).
                filter(RuleAssetAllocation.AllocationPercentage >= 1).
                where(RuleAssetAllocation.IsDeleted == False)

        )
        return_items = []

        for item in result.fetchall():
            return_items.append(item)
        if not return_items:
            raise DoesNotExist(f"Data does not exist")
        listings = {k : list(g) for k, g in groupby(return_items, attrgetter('assetClass'))}

        return listings

