from datetime import datetime
from typing import Type

import uuid

from sqlalchemy import update, select
from sqlalchemy.dialects.postgresql import insert

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_rental_income_data import NetWorthRentalIncomeData
from app.db.tables.net_worth_user_table_data import NetWorthUserTableData
from app.models.schema.net_worth_rental_income_data import NetWorthRentalIncomeDataSchemaBase, \
    NetWorthRentalIncomeDataSchema, InNetWorthRentalIncomeDataSchema


class NetWorthRentalIncomeDataRepository(
    BaseRepository[NetWorthRentalIncomeDataSchemaBase, NetWorthRentalIncomeDataSchema, NetWorthRentalIncomeData]):
    @property
    def _in_schema(self) -> Type[NetWorthRentalIncomeDataSchemaBase]:
        return InNetWorthRentalIncomeDataSchema

    @property
    def _schema(self) -> Type[NetWorthRentalIncomeDataSchema]:
        return NetWorthRentalIncomeDataSchema

    @property
    def _table(self) -> Type[NetWorthRentalIncomeData]:
        return NetWorthRentalIncomeData

    async def create_and_save(self, payload: InNetWorthRentalIncomeDataSchema):
        table_id = uuid.uuid4()
        stmt = (insert(NetWorthUserTableData).values(
            Id=table_id,
            UserId=payload.UserId,
            CategoryId=payload.CategoryId,
            InvestmentBucketId=payload.BucketId,
            Property=payload.Property,
            RentalInflation=payload.RentalInflation,
            RentalIncomePerYear=payload.RentalIncomePerYear,
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

    async def update_data(self, payload: NetWorthRentalIncomeDataSchema):
        stmt = (update(NetWorthUserTableData).values(
            CategoryId=payload.CategoryId,
            InvestmentBucketId=payload.BucketId,
            Property=payload.Property,
            RentalInflation=payload.RentalInflation,
            RentalIncomePerYear=payload.RentalIncomePerYear,
            CreatedOn=datetime.now(),
            UpdatedOn=datetime.now(),
            IsDeleted=False
        ).where(UserId=payload.Id))

        return await self._db_session.execute(stmt)

    async def get_data(self, user_id, category_id):
        stmt = (select(NetWorthUserTableData.AssetName, NetWorthUserTableData.TodaysValue,
                       NetWorthUserTableData.PlannedForLiquidity, NetWorthUserTableData.TargetLiquidityYear,
                       NetWorthUserTableData.ExpectedPrice)
                .where(UserId=user_id, CategoryID=category_id))

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

        return []

    async def delete(self, user_id):
        stmt = (update(NetWorthUserTableData).values(
            IsDeleted=False
        ).where(UserId=user_id))

        return await self._db_session.execute(stmt)
