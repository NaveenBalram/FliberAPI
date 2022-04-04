from typing import Type

from sqlalchemy import select, and_

from app.db.repositories.base import BaseRepository
from app.db.tables.funds_category import FundsCategory
from app.models.schema.funds_category import (
    FundsCategorySchemaBase,
    FundsCategorySchema,
    InFundsCategorySchema,
)


class FundsCategoryRepository(
    BaseRepository[FundsCategorySchemaBase, FundsCategorySchema, FundsCategory]
):
    @property
    def _in_schema(self) -> Type[FundsCategorySchemaBase]:
        return InFundsCategorySchema

    @property
    def _schema(self) -> Type[FundsCategorySchema]:
        return FundsCategorySchema

    @property
    def _table(self) -> Type[FundsCategory]:
        return FundsCategory

    def get_by_asset_id(self, user_id, asset_id):
        pass

    async def get_by_type(self, rp_type, amount):

        if amount > 20000:
            query = and_(
                self._table.Type == rp_type,
                self._table.MinAmount == 20000,
                self._table.MaxAmount == 20000,
            )
        else:
            query = and_(
                self._table.Type == rp_type,
                self._table.MinAmount <= amount,
                self._table.MaxAmount >= amount,
            )

        stmt = select(self._table).where(query)

        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            return_items.append(item[0].__dict__)

        return return_items
