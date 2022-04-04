import uuid
from datetime import datetime
from typing import Type

from sqlalchemy import insert, select, update

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_life_insurance_data import NetWorthLifeInsuranceData
from app.db.tables.net_worth_user_table_data import NetWorthUserTableData
from app.models.schema.net_worth_life_insurance_data import NetWorthLifeInsuranceDataSchemaBase, \
    NetWorthLifeInsuranceDataSchema, InNetWorthLifeInsuranceDataSchema


class NetWorthLifeInsuranceDataRepository(
    BaseRepository[NetWorthLifeInsuranceDataSchemaBase, NetWorthLifeInsuranceDataSchema, NetWorthLifeInsuranceData]):

    @property
    def _in_schema(self) -> Type[NetWorthLifeInsuranceDataSchemaBase]:
        return InNetWorthLifeInsuranceDataSchema

    @property
    def _schema(self) -> Type[NetWorthLifeInsuranceDataSchema]:
        return NetWorthLifeInsuranceDataSchema

    @property
    def _table(self) -> Type[NetWorthLifeInsuranceData]:
        return NetWorthLifeInsuranceData

    async def create_and_save(self, payload: InNetWorthLifeInsuranceDataSchema):
        table_id = uuid.uuid4()
        stmt = (insert(NetWorthUserTableData).values(Id=table_id,
                                                     UserId=payload.UserId,
                                                     CategoryId=payload.CategoryId,
                                                     InvestmentBucketId=payload.BucketId,
                                                     PolicyProvider=payload.PolicyProvider,
                                                     SchemaName=payload.SchemaName,
                                                     PolicyNumber=payload.PolicyNumber,
                                                     PolicyType=payload.PolicyType,
                                                     StartDate=payload.StartDate,
                                                     PolicyTerm=payload.PolicyTerm,
                                                     SumAssured=payload.SumAssured,
                                                     MaturityValue=payload.MaturityValue,
                                                     CreatedOn=datetime.now(),
                                                     UpdatedOn=datetime.now(),
                                                     IsDeleted=False
                                                     ))

        await self._db_session.execute(stmt)

        stmt = (
            select(NetWorthUserTableData.Id, NetWorthUserTableData.CategoryId, NetWorthUserTableData.InvestmentBucketId,
                   NetWorthUserTableData.PolicyProvider, NetWorthUserTableData.SchemaName,
                   NetWorthUserTableData.PolicyNumber, NetWorthUserTableData.PolicyType,
                   NetWorthUserTableData.StartDate, NetWorthUserTableData.PolicyTerm,
                   NetWorthUserTableData.SumAssured, NetWorthUserTableData.MaturityValue,
                   NetWorthUserTableData.CreatedOn,
                   NetWorthUserTableData.UpdatedOn).where(NetWorthUserTableData.Id == table_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        return []

    async def update_data(self, payload: NetWorthLifeInsuranceDataSchema):
        stmt = (update(NetWorthUserTableData).values(
            CategoryId=payload.CategoryId,
            InvestmentBucketId=payload.BucketId,
            PolicyProvider=payload.PolicyProvider,
            SchemaName=payload.SchemaName,
            PolicyNumber=payload.PolicyNumber,
            PolicyType=payload.PolicyType,
            StartDate=payload.StartDate,
            PolicyTerm=payload.PolicyTerm,
            SumAssured=payload.SumAssured,
            MaturityValue=payload.MaturityValue,
            CreatedOn=datetime.now(),
            UpdatedOn=datetime.now(),
            IsDeleted=False
        ).where(UserId=payload.Id))

        return await self._db_session.execute(stmt)

    async def get_data(self, user_id, category_id, bucket_id):
        stmt = (select(NetWorthUserTableData.PolicyProvider, NetWorthUserTableData.SchemaName,
                       NetWorthUserTableData.PolicyNumber, NetWorthUserTableData.PolicyType,
                       NetWorthUserTableData.StartDate, NetWorthUserTableData.PolicyTerm,
                       NetWorthUserTableData.SumAssured, NetWorthUserTableData.MaturityValue)
                .where(UserId=user_id, CategoryID=category_id, InvestmentBucketId=bucket_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        return []

    async def get_all_data(self, user_id):
        stmt = (select(NetWorthUserTableData.PolicyProvider, NetWorthUserTableData.SchemaName,
                       NetWorthUserTableData.PolicyNumber, NetWorthUserTableData.PolicyType,
                       NetWorthUserTableData.StartDate, NetWorthUserTableData.PolicyTerm,
                       NetWorthUserTableData.SumAssured, NetWorthUserTableData.MaturityValue).where(UserId=user_id))

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
