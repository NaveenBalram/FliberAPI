import uuid
from datetime import datetime
from typing import Type

from sqlalchemy import insert, update, select

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_loan_data import NetWorthLoanData
from app.db.tables.net_worth_user_table_data import NetWorthUserTableData
from app.models.schema.net_worth_loan_data import NetWorthLoanDataSchemaBase, NetWorthLoanDataSchema, \
    InNetWorthLoanDataSchema


class NetWorthLoanDataRepository(BaseRepository[NetWorthLoanDataSchemaBase, NetWorthLoanDataSchema, NetWorthLoanData]):
    @property
    def _in_schema(self) -> Type[NetWorthLoanDataSchemaBase]:
        return InNetWorthLoanDataSchema

    @property
    def _schema(self) -> Type[NetWorthLoanDataSchema]:
        return NetWorthLoanDataSchema

    @property
    def _table(self) -> Type[NetWorthLoanData]:
        return NetWorthLoanData

    async def create_and_save(self, payload: InNetWorthLoanDataSchema):
        stmt = (insert(NetWorthUserTableData).values(Id=uuid.uuid4(),
                                                     UserId=payload.UserId,
                                                     CategoryId=payload.CategoryId,
                                                     InvestmentBucketId=payload.BucketId,
                                                     LoanType=payload.LoanType,
                                                     LenderName=payload.LenderName,
                                                     StartYear=payload.StartYear,
                                                     EndYear=payload.EndYear,
                                                     OutStandingAmount=payload.OutStandingAmount,
                                                     CreatedOn=datetime.now(),
                                                     UpdatedOn=datetime.now(),
                                                     IsDeleted=False
                                                     ))

        return await self._db_session.execute(stmt)

    async def update_data(self, payload: NetWorthLoanDataSchema):
        stmt = (update(NetWorthUserTableData).values(
            CategoryId=payload.CategoryId,
            InvestmentBucketId=payload.BucketId,
            LoanType=payload.LoanType,
            LenderName=payload.LenderName,
            StartYear=payload.StartYear,
            EndYear=payload.EndYear,
            OutStandingAmount=payload.OutStandingAmount,
            CreatedOn=datetime.now(),
            UpdatedOn=datetime.now(),
            IsDeleted=False
        ).where(UserId=payload.Id))

        return await self._db_session.execute(stmt)

    async def get_data(self, user_id, category_id):
        stmt = (select(NetWorthUserTableData.LoanType, NetWorthUserTableData.Lender,
                       NetWorthUserTableData.StartYear, NetWorthUserTableData.EndYear,
                       NetWorthUserTableData.OutStandingAmount)
                .where(UserId=user_id, CategoryID=category_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        return []

    async def get_all_data(self, user_id):
        stmt = (select(NetWorthUserTableData.LoanType, NetWorthUserTableData.Lender,
                       NetWorthUserTableData.StartYear, NetWorthUserTableData.EndYear,
                       NetWorthUserTableData.OutStandingAmount).where(UserId=user_id))

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
