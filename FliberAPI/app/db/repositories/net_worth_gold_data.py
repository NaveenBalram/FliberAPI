import uuid
from datetime import datetime
from typing import Type

from sqlalchemy import insert, update, select

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_gold_data import NetWorthGoldData
from app.db.tables.net_worth_user_table_data import NetWorthUserTableData
from app.models.schema.net_worth_gold_data import NetWorthGoldDataSchemaBase, NetWorthGoldDataSchema, \
    InNetWorthGoldDataSchema


class NetWorthGoldDataRepository(BaseRepository[NetWorthGoldDataSchemaBase, NetWorthGoldDataSchema, NetWorthGoldData]):
    @property
    def _in_schema(self) -> Type[NetWorthGoldDataSchemaBase]:
        return InNetWorthGoldDataSchema

    @property
    def _schema(self) -> Type[NetWorthGoldDataSchema]:
        return NetWorthGoldDataSchema

    @property
    def _table(self) -> Type[NetWorthGoldData]:
        return NetWorthGoldData

    async def create_and_save(self, payload: InNetWorthGoldDataSchema):
        table_id = uuid.uuid4()
        stmt = (insert(NetWorthUserTableData).values(Id=table_id,
                                                     UserId=payload.UserId,
                                                     CategoryId=payload.CategoryId,
                                                     InvestmentBucketId=payload.BucketId,
                                                     TodaysValue=payload.TodaysValue,
                                                     CreatedOn=datetime.now(),
                                                     UpdatedOn=datetime.now(),
                                                     IsDeleted=False
                                                     ))

        await self._db_session.execute(stmt)
        await self._db_session.commit()

        stmt = (
            select(NetWorthUserTableData.Id, NetWorthUserTableData.CategoryId, NetWorthUserTableData.InvestmentBucketId,
                   NetWorthUserTableData.TodaysValue, NetWorthUserTableData.CreatedOn,
                   NetWorthUserTableData.UpdatedOn).where(NetWorthUserTableData.Id == table_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        return []

    async def update_data(self, payload: NetWorthGoldDataSchema):
        stmt = (update(NetWorthUserTableData).values(
            UserId=payload.UserId,
            CategoryId=payload.CategoryId,
            InvestmentBucketId=payload.BucketId,
            TodaysValue=payload.TodaysValue,
            UpdatedOn=datetime.now(),
            IsDeleted=False
        ).where(UserId=payload.Id))

        return await self._db_session.execute(stmt)

    async def get_data(self, user_id, category_id):
        stmt = (select(
            NetWorthUserTableData.TodaysValue,
        ).where(UserId=user_id, CategoryID=category_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        return []

    async def get_all_data(self):
        stmt = (select(NetWorthUserTableData.UserId, NetWorthUserTableData.CategoryId,
                       NetWorthUserTableData.InvestmentBucketId, NetWorthUserTableData.TodaysValue))

        result = await self._db_session.execute(stmt)
        return_data = []
        for data in result.fetchall():
            return_data.append(data)

        return return_data

    async def delete(self, user_id):
        stmt = (update(NetWorthUserTableData).values(
            IsDeleted=False
        ).where(UserId=user_id))

        return await self._db_session.execute(stmt)
