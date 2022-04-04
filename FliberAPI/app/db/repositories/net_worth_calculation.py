import datetime
from typing import Type

from sqlalchemy import select, insert

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_calculation import NetWorthCalculation
from app.db.tables.net_worth_user_table_data import NetWorthUserTableData
from app.models.schema.net_worth_calculation import NetWorthCalculationSchemaBase, NetWorthCalculationSchema, \
    InNetWorthCalculationSchema


class NetWorthCalculationRepository(
    BaseRepository[NetWorthCalculationSchemaBase, NetWorthCalculationSchema, NetWorthCalculation]):
    @property
    def _in_schema(self) -> Type[NetWorthCalculationSchemaBase]:
        return InNetWorthCalculationSchema

    @property
    def _schema(self) -> Type[NetWorthCalculationSchema]:
        return NetWorthCalculationSchema

    @property
    def _table(self) -> Type[NetWorthCalculation]:
        return NetWorthCalculation

    async def get_data_by_id(self, uuid):
        stmt = (select(NetWorthUserTableData.TodaysValue, NetWorthUserTableData.OutStandingAmount,
                       NetWorthUserTableData.EstimatedValue, NetWorthUserTableData.PrincipalAmount,
                       NetWorthUserTableData.SumAssured).where(NetWorthUserTableData.UserId == uuid))

        result = await self._db_session.execute(stmt)
        total = 0
        outstanding = 0
        for data in result.fetchall():
            if data.TodaysValue or data.EstimatedValue or data.PrincipalAmount or data.SumAssured:
                total += data.TodaysValue

            if data.OutStandingAmount:
                outstanding += data.OutStandingAmount

        net_worth = total - outstanding

        stmt = (insert(NetWorthCalculation).values(Id=uuid.uuid4(), UserId=uuid, NetWorthAmount=net_worth,
                                                   CreatedOn=datetime.datetime.now(),
                                                   UpdatedOn=datetime.datetime.now(),
                                                   IsDeleted=False))

        await self._db_session.execute(stmt)

        return net_worth
