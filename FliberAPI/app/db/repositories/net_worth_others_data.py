import uuid
from datetime import datetime
from typing import Type

from sqlalchemy import update, select
from sqlalchemy.dialects.postgresql import insert

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_others_data import NetWorthOthersData
from app.db.tables.net_worth_user_table_data import NetWorthUserTableData
from app.models.schema.net_worth_others_data import NetWorthOthersDataSchemaBase, NetWorthOthersDataSchema, \
    InNetWorthOthersDataSchema


class NetWorthOthersDataRepository(
    BaseRepository[NetWorthOthersDataSchemaBase, NetWorthOthersDataSchema, NetWorthOthersData]):
    @property
    def _in_schema(self) -> Type[NetWorthOthersDataSchemaBase]:
        return InNetWorthOthersDataSchema

    @property
    def _schema(self) -> Type[NetWorthOthersDataSchema]:
        return NetWorthOthersDataSchema

    @property
    def _table(self) -> Type[NetWorthOthersData]:
        return NetWorthOthersData

    async def create_and_save(self, payload: InNetWorthOthersDataSchema):
        table_id = uuid.uuid4()
        stmt = (insert(NetWorthUserTableData).values(
            Id=table_id,
            UserId=payload.UserId,
            CategoryId=payload.CategoryId,
            InvestmentBucketId=payload.BucketId,
            AssetName=payload.AssetName,
            TodaysValue=payload.TodaysValue,
            PlannedForLiquidityFlag=payload.PlannedForLiquidity,
            TargetLiquidityYear=payload.TargetLiquidityYear,
            ExpectedPrice=payload.ExpectedPrice,
            CreatedOn=datetime.now(),
            UpdatedOn=datetime.now(),
            IsDeleted=False
        ))

        await self._db_session.execute(stmt)

        stmt = (
            select(NetWorthUserTableData.Id, NetWorthUserTableData.CategoryId, NetWorthUserTableData.InvestmentBucketId,
                   NetWorthUserTableData.AssetName, NetWorthUserTableData.TodaysValue,
                   NetWorthUserTableData.PlannedForLiquidity, NetWorthUserTableData.TargetLiquidityYear,
                   NetWorthUserTableData.ExpectedPrice,
                   NetWorthUserTableData.CreatedOn,
                   NetWorthUserTableData.UpdatedOn).where(NetWorthUserTableData.Id == table_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        return []

    async def update_data(self, payload: NetWorthOthersDataSchema):
        stmt = (update(NetWorthUserTableData).values(
            CategoryId=payload.CategoryId,
            InvestmentBucketId=payload.BucketId,
            AssetName=payload.AssetName,
            TodaysValue=payload.TodaysValue,
            PlannedForLiquidity=payload.PlannedForLiquidity,
            TargetLiquidityYear=payload.TargetLiquidityYear,
            ExpectedPrice=payload.ExpectedPrice,
            CreatedOn=datetime.now(),
            UpdatedOn=datetime.now(),
            IsDeleted=False
        ).where(UserId=payload.Id))

        return await self._db_session.execute(stmt)

    async def get_data(self, user_id, category_id, bucket_id):
        stmt = (select(NetWorthUserTableData.AssetName, NetWorthUserTableData.TodaysValue,
                       NetWorthUserTableData.PlannedForLiquidity, NetWorthUserTableData.TargetLiquidityYear,
                       NetWorthUserTableData.ExpectedPrice)
                .where(UserId=user_id, CategoryID=category_id, InvestmentBucketId=bucket_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        return []

    async def get_all_data(self, user_id):
        stmt = (select(NetWorthUserTableData.AccountNumber, NetWorthUserTableData.BankName,
                       NetWorthUserTableData.CurrentBalance).where(UserId=user_id))

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
