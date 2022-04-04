import uuid
from datetime import datetime
from typing import Type

from sqlalchemy import select, update, insert

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_fixed_deposit_data import NetWorthFixedDepositData
from app.db.tables.net_worth_user_table_data import NetWorthUserTableData
from app.models.schema.net_worth_fixed_deposit_data import NetWorthFixedDepositDataSchemaBase, \
    NetWorthFixedDepositDataSchema, InNetWorthFixedDepositDataSchema


class NetWorthFixedDepositDataRepository(
    BaseRepository[NetWorthFixedDepositDataSchemaBase, NetWorthFixedDepositDataSchema, NetWorthFixedDepositData]):

    @property
    def _in_schema(self) -> Type[NetWorthFixedDepositDataSchemaBase]:
        return InNetWorthFixedDepositDataSchema

    @property
    def _schema(self) -> Type[NetWorthFixedDepositDataSchema]:
        return NetWorthFixedDepositDataSchema

    @property
    def _table(self) -> Type[NetWorthFixedDepositData]:
        return NetWorthFixedDepositData

    async def create_and_save(self, payload: InNetWorthFixedDepositDataSchema):
        table_id = uuid.uuid4()
        stmt = (insert(NetWorthUserTableData).values(Id=uuid.uuid4(),
                                                     UserId=payload.UserId,
                                                     CategoryId=payload.CategoryId,
                                                     InvestmentBucketId=payload.BucketId,
                                                     AccountNumber=payload.AccountNumber,
                                                     MaturityDate=payload.MaturityDate,
                                                     PrincipalAmount=payload.PrincipalAmount,
                                                     MaturityAmount=payload.MaturityAmount,
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
                   NetWorthUserTableData.PrincipalAmount,
                   NetWorthUserTableData.MaturityDate,
                   NetWorthUserTableData.MaturityAmount,
                   NetWorthUserTableData.CreatedOn,
                   NetWorthUserTableData.UpdatedOn).where(NetWorthUserTableData.Id == table_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        return []

    async def update_data(self, payload: NetWorthFixedDepositDataSchema):
        stmt = (update(NetWorthUserTableData).values(
            CategoryId=payload.CategoryId,
            InvestmentBucketId=payload.BucketId,
            AccountNumber=payload.AccountNumber,
            MaturityDate=payload.MaturityDate,
            PrincipalAmount=payload.PrincipalAmount,
            MaturityAmount=payload.MaturityAmount,
            CreatedOn=datetime.now(),
            UpdatedOn=datetime.now(),
            IsDeleted=False
        ).where(UserId=payload.Id))

        return await self._db_session.execute(stmt)

    async def get_data(self, user_id, category_id):
        stmt = (select(NetWorthUserTableData.AccountNumber, NetWorthUserTableData.PrincipalAmount,
                       NetWorthUserTableData.MaturityDate, NetWorthUserTableData.MaturityAmount)
                .where(UserId=user_id, CategoryID=category_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data[0]

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
