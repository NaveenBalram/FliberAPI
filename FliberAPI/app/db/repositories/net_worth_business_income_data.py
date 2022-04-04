import uuid
from datetime import datetime
from typing import Type

from sqlalchemy import insert, update, select

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_business_income_data import NetWorthBusinessIncomeData
from app.db.tables.net_worth_user_table_data import NetWorthUserTableData
from app.models.schema.net_worth_business_income_data import NetWorthBusinessIncomeDataSchemaBase, \
    NetWorthBusinessIncomeDataSchema, InNetWorthBusinessIncomeDataSchema


class NetWorthBusinessIncomeDataRepository(
    BaseRepository[NetWorthBusinessIncomeDataSchemaBase, NetWorthBusinessIncomeDataSchema, NetWorthBusinessIncomeData]):
    @property
    def _in_schema(self) -> Type[NetWorthBusinessIncomeDataSchemaBase]:
        return InNetWorthBusinessIncomeDataSchema

    @property
    def _schema(self) -> Type[NetWorthBusinessIncomeDataSchema]:
        return NetWorthBusinessIncomeDataSchema

    @property
    def _table(self) -> Type[NetWorthBusinessIncomeData]:
        return NetWorthBusinessIncomeData

    async def create_and_save(self, payload: InNetWorthBusinessIncomeDataSchema):
        table_id = uuid.uuid4()
        stmt = (insert(NetWorthUserTableData).values(Id=table_id,
                                                     UserId=payload.UserId,
                                                     CategoryId=payload.CategoryId,
                                                     InvestmentBucketId=payload.BucketId,
                                                     Description=payload.Description,
                                                     YearlyAmount=payload.YearlyAmount,
                                                     CreatedOn=datetime.now(),
                                                     UpdatedOn=datetime.now(),
                                                     IsDeleted=False
                                                     ))

        await self._db_session.execute(stmt)
        stmt = (
            select(NetWorthUserTableData.Id,
                   NetWorthUserTableData.CategoryId,
                   NetWorthUserTableData.InvestmentBucketId,
                   NetWorthUserTableData.UserId,
                   NetWorthUserTableData.AccountNumber,
                   NetWorthUserTableData.BankName,
                   NetWorthUserTableData.CurrentBalance,
                   NetWorthUserTableData.CreatedOn,
                   NetWorthUserTableData.UpdatedOn).where(NetWorthUserTableData.Id == table_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        return []

    async def update_data(self, payload: NetWorthBusinessIncomeDataSchema):
        stmt = (update(NetWorthUserTableData).values(
            UserId=payload.UserId,
            CategoryId=payload.CategoryId,
            InvestmentBucketId=payload.BucketId,
            Description=payload.Description,
            YearlyAmount=payload.YearlyAmount,
            CreatedOn=datetime.now(),
            UpdatedOn=datetime.now(),
            IsDeleted=False
        ).where(UserId=payload.Id))

        return await self._db_session.execute(stmt)

    async def get_data(self, user_id, category_id):
        stmt = (select(NetWorthUserTableData.Description, NetWorthUserTableData.YearlyAmount,
                       ).where(UserId=user_id, CategoryID=category_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        return []

    async def get_all_data(self, user_id):
        stmt = (select(NetWorthUserTableData.Description, NetWorthUserTableData.YearlyAmount,
                       ).where(UserId=user_id))

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
