from typing import Type

from sqlalchemy import and_
from sqlalchemy.future import select

from app.db.errors import DoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.tables.target_assets import TargetAssets
from app.models.schema.target_assets import (
    TargetAssetsSchemaBase,
    TargetAssetsSchema,
    InTargetAssetsSchema,
)


class TargetAssetsRepository(
    BaseRepository[TargetAssetsSchemaBase, TargetAssetsSchema, TargetAssets]
):
    @property
    def _in_schema(self) -> Type[TargetAssetsSchemaBase]:
        return InTargetAssetsSchema

    @property
    def _schema(self) -> Type[TargetAssetsSchema]:
        return TargetAssetsSchema

    @property
    def _table(self) -> Type[TargetAssets]:
        return TargetAssets

    async def get_asset(self, payload):
        result = await self._db_session.execute(
            select(self._table.Debt, self._table.Gold, self._table.Equity).where(
                self._table.Name == payload["Name"], self._table.Type == payload["Type"]
            )
        )
        return_items = []
        for item in result.fetchall():
            return_items.append(item[0])
        if not return_items:
            raise DoesNotExist(f"Data does not exist")
        return return_items

    async def get_by_age_limit(self, age, target_type, amount):
        if amount > 20000:
            amount = 20000
        print("Amount", age, amount, target_type)
        result = await self._db_session.execute(
            select(self._table).where(
                and_(
                    self._table.MinAgeLimit <= age,
                    self._table.MaxAgeLimit >= age,
                    self._table.MinAmount <= amount,
                    self._table.MaxAmount >= amount,
                    self._table.Type == target_type,
                )
            )
        )
        return_items = []
        for item in result.fetchall():
            return item[0].__dict__
        return return_items

    async def get_limit_by_type(self, rp_type):

        stmt = select(self._table.MinAgeLimit).where(self._table.Type == rp_type)

        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            return_items.append(item)

        return return_items
