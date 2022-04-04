from typing import Type

from sqlalchemy import update

from app.db.repositories.base import BaseRepository
from app.db.tables.user_assets import UserAssets
from app.models.schema.user_assets import (
    UserAssetsSchemaBase,
    UserAssetsSchema,
    InUserAssetsSchema,
)


class UserAssetsRepository(
    BaseRepository[UserAssetsSchemaBase, UserAssetsSchema, UserAssets]
):
    @property
    def _in_schema(self) -> Type[UserAssetsSchemaBase]:
        return InUserAssetsSchema

    @property
    def _schema(self) -> Type[UserAssetsSchema]:
        return UserAssetsSchema

    @property
    def _table(self) -> Type[UserAssets]:
        return UserAssets

    async def update_units(self, user_id, fund, units):
        print(user_id, fund, units)
        stmt = (
            update(self._table)
            .where(self._table.UserId == user_id, self._table.FundName == fund)
            .values(NoOfUnits=units, IsDeleted=False)
        )
        await self._db_session.execute(stmt)
        await self._db_session.commit()

    async def set_delete(self, user_id):

        stmt = (
            update(self._table)
            .where(self._table.UserId == user_id)
            .values(IsDeleted=True)
        )
        await self._db_session.execute(stmt)
        await self._db_session.commit()
