import uuid
from datetime import datetime
from typing import Type

from sqlalchemy import insert, update, select

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_house_data import NetWorthHouseData
from app.db.tables.net_worth_user_table_data import NetWorthUserTableData
from app.models.schema.net_worth_house_data import NetWorthHouseDataSchemaBase, NetWorthHouseDataSchema, \
    InNetWorthHouseDataSchema


class NetWorthHouseDataRepository(
    BaseRepository[NetWorthHouseDataSchemaBase, NetWorthHouseDataSchema, NetWorthHouseData]):
    @property
    def _in_schema(self) -> Type[NetWorthHouseDataSchemaBase]:
        return InNetWorthHouseDataSchema

    @property
    def _schema(self) -> Type[NetWorthHouseDataSchema]:
        return NetWorthHouseDataSchema

    @property
    def _table(self) -> Type[NetWorthHouseData]:
        return NetWorthHouseData

    async def create_and_save(self, payload: InNetWorthHouseDataSchema):

        table_id = uuid.uuid4()
        stmt = (insert(NetWorthUserTableData).values(Id=table_id,
                                                     UserId=payload.UserId,
                                                     CategoryId=payload.CategoryId,
                                                     InvestmentBucketId=payload.BucketId,
                                                     Description=payload.Description,
                                                     PropertyLocation=payload.PropertyLocation,
                                                     SopLop=payload.SOPLOP,
                                                     RegistrationYear=payload.RegistrationYear,
                                                     TodaysValue=payload.TodaysValue,
                                                     PlannedForLiquidityFlag=payload.PlannedForLiquidityFlag,
                                                     TargetLiquidityYear=payload.TargetLiquidityYear,
                                                     ExpectedPrice=payload.ExpectedPrice,
                                                     CreatedOn=datetime.now(),
                                                     UpdatedOn=datetime.now(),
                                                     IsDeleted=False
                                                     ))

        await self._db_session.execute(stmt)

        stmt = (
            select(NetWorthUserTableData.Id, NetWorthUserTableData.CategoryId, NetWorthUserTableData.InvestmentBucketId,
                   NetWorthUserTableData.Description,
                   NetWorthUserTableData.PropertyLocation,
                   NetWorthUserTableData.SopLop,
                   NetWorthUserTableData.RegistrationYear,
                   NetWorthUserTableData.TodaysValue,
                   NetWorthUserTableData.PlannedForLiquidityFlag,
                   NetWorthUserTableData.TargetLiquidityYear,
                   NetWorthUserTableData.ExpectedPrice, NetWorthUserTableData.CreatedOn,
                   NetWorthUserTableData.UpdatedOn).where(NetWorthUserTableData.Id == table_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        return []

    async def update_data(self, payload: NetWorthHouseDataSchema):
        stmt = (update(NetWorthUserTableData).values(
            CategoryId=payload.CategoryId,
            InvestmentBucketId=payload.BucketId,
            Description=payload.Description,
            PropertyLocation=payload.PropertyLocation,
            SopLop=payload.SOPLOP,
            RegistrationYear=payload.RegistrationYear,
            TodaysValue=payload.TodaysValue,
            PlannedForLiquidityFlag=payload.PlannedForLiquidityFlag,
            TargetLiquidityYear=payload.TargetLiquidityYear,
            ExpectedPrice=payload.ExpectedPrice,
            CreatedOn=datetime.now(),
            UpdatedOn=datetime.now(),
            IsDeleted=False
        ).where(UserId=payload.Id))

        return await self._db_session.execute(stmt)

    async def get_data(self, user_id, category_id):
        stmt = (select(
            NetWorthUserTableData.Description,
            NetWorthUserTableData.PropertyLocation,
            NetWorthUserTableData.SopLop,
            NetWorthUserTableData.RegistrationYear,
            NetWorthUserTableData.TodaysValue,
            NetWorthUserTableData.PlannedForLiquidityFlag,
            NetWorthUserTableData.TargetLiquidityYear,
            NetWorthUserTableData.ExpectedPrice
        ).where(UserId=user_id, CategoryID=category_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        return []

    async def get_all_data(self, user_id):
        stmt = (select(NetWorthUserTableData.AssetName, NetWorthUserTableData.TodaysValue,
                       NetWorthUserTableData.PlannedForLiquidityFlag, NetWorthUserTableData.ExpectedPrice).where(
            UserId=user_id))

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
