import uuid
from datetime import datetime
from typing import Type

from sqlalchemy import insert, update, select

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_investment_data import NetWorthInvestmentData
from app.db.tables.net_worth_user_table_data import NetWorthUserTableData
from app.models.schema.net_worth_investment_data import NetWorthInvestmentDataSchemaBase, NetWorthInvestmentDataSchema, \
    InNetWorthInvestmentDataSchema


class NetWorthInvestmentDataRepository(
    BaseRepository[NetWorthInvestmentDataSchemaBase, NetWorthInvestmentDataSchema, NetWorthInvestmentData]):

    @property
    def _in_schema(self) -> Type[NetWorthInvestmentDataSchemaBase]:
        return InNetWorthInvestmentDataSchema

    @property
    def _schema(self) -> Type[NetWorthInvestmentDataSchema]:
        return NetWorthInvestmentDataSchema

    @property
    def _table(self) -> Type[NetWorthInvestmentData]:
        return NetWorthInvestmentData

    async def create_and_save(self, payload: InNetWorthInvestmentDataSchema):
        table_id = uuid.uuid4()
        stmt = (insert(NetWorthUserTableData).values(Id=table_id,
                                                     UserId=payload.UserId,
                                                     CategoryId=payload.CategoryId,
                                                     InvestmentBucketId=payload.BucketId,
                                                     AccountNumber=payload.AccountNumber,
                                                     StartDate=payload.StartDate,
                                                     MaturityDate=payload.MaturityDate,
                                                     PrincipalAmount=payload.PrincipalAmount,
                                                     MaturityAmount=payload.MaturityAmount,
                                                     CreatedOn=datetime.now(),
                                                     UpdatedOn=datetime.now(),
                                                     IsDeleted=False
                                                     ))

        await self._db_session.execute(stmt)

        stmt = (
            select(NetWorthUserTableData.Id, NetWorthUserTableData.CategoryId, NetWorthUserTableData.InvestmentBucketId,
                   NetWorthUserTableData.AccountNumber, NetWorthUserTableData.StartDate,
                   NetWorthUserTableData.MaturityDate, NetWorthUserTableData.PrincipalAmount,
                   NetWorthUserTableData.MaturityAmount, NetWorthUserTableData.CreatedOn,
                   NetWorthUserTableData.UpdatedOn).where(NetWorthUserTableData.Id == table_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        return []

    async def update_data(self, payload: NetWorthInvestmentDataSchema):
        stmt = (update(NetWorthUserTableData).values(
            CategoryId=payload.CategoryId,
            InvestmentBucketId=payload.BucketId,
            AccountNumber=payload.AccountNumber,
            StartDate=payload.StartDate,
            MaturityDate=payload.MaturityDate,
            PrincipalAmount=payload.PrincipalAmount,
            MaturityAmount=payload.MaturityAmount,
            CreatedOn=datetime.now(),
            UpdatedOn=datetime.now(),
            IsDeleted=False
        ).where(UserId=payload.Id))

        return await self._db_session.execute(stmt)

    async def get_data(self, user_id, category_id, bucket_id):
        stmt = (select(NetWorthUserTableData.AccountNumber, NetWorthUserTableData.StartDate,
                       NetWorthUserTableData.MaturityDate, NetWorthUserTableData.PrincipalAmount,
                       NetWorthUserTableData.MaturityAmount)
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
