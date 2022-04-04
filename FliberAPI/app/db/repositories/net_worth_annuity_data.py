import uuid
from datetime import datetime
from typing import Type

from sqlalchemy import insert, update, select

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_annuity_data import NetWorthAnnuityData
from app.db.tables.net_worth_user_table_data import NetWorthUserTableData
from app.models.schema.net_worth_annuity_data import NetWorthAnnuityDataSchemaBase, NetWorthAnnuityDataSchema, \
    InNetWorthAnnuityDataSchema


class NetWorthAnnuityDataRepository(
    BaseRepository[NetWorthAnnuityDataSchemaBase, NetWorthAnnuityDataSchema, NetWorthAnnuityData]):
    @property
    def _in_schema(self) -> Type[NetWorthAnnuityDataSchemaBase]:
        return InNetWorthAnnuityDataSchema

    @property
    def _schema(self) -> Type[NetWorthAnnuityDataSchema]:
        return NetWorthAnnuityDataSchema

    @property
    def _table(self) -> Type[NetWorthAnnuityData]:
        return NetWorthAnnuityData

    async def create_and_save(self, payload: InNetWorthAnnuityDataSchema):
        table_id = uuid.uuid4()
        stmt = (insert(NetWorthUserTableData).values(Id=table_id,
                                                     UserId=payload.UserId,
                                                     CategoryId=payload.CategoryId,
                                                     InvestmentBucketId=payload.BucketId,
                                                     AccountNumber=payload.AccountNumber,
                                                     SchemeName=payload.SchemeName,
                                                     StartDate=payload.StartDate,
                                                     SchemeType=payload.SchemeType,
                                                     Corpus=payload.Corpus,
                                                     AnnuityIncome=payload.AnnuityIncome,
                                                     GrowthOfPension=payload.GrowthOfPension,
                                                     nnuityMaturity=payload.AnnuityMaturity,
                                                     Frequency=payload.Frequency,
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
                   NetWorthUserTableData.SchemeName,
                   NetWorthUserTableData.StartDate,
                   NetWorthUserTableData.SchemeType,
                   NetWorthUserTableData.Corpus,
                   NetWorthUserTableData.AnnuityIncome,
                   NetWorthUserTableData.GrowthOfPension,
                   NetWorthUserTableData.AnnuityMaturity,
                   NetWorthUserTableData.Frequency,
                   NetWorthUserTableData.CreatedOn,
                   NetWorthUserTableData.UpdatedOn).where(NetWorthUserTableData.Id == table_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        return []

    async def update_data(self, payload: NetWorthAnnuityDataSchema):
        stmt = (update(NetWorthUserTableData).values(
            Id=payload.Id,
            UserId=payload.UserId,
            CategoryId=payload.CategoryId,
            InvestmentBucketId=payload.BucketId,
            AccountNumber=payload.AccountNumber,
            SchemeName=payload.SchemeName,
            StartDate=payload.StartDate,
            SchemeType=payload.SchemeType,
            Corpus=payload.Corpus,
            AnnuityIncome=payload.AnnuityIncome,
            GrowthOfPension=payload.GrowthOfPension,
            nnuityMaturity=payload.AnnuityMaturity,
            Frequency=payload.Frequency,
            UpdatedOn=datetime.now(),
            IsDeleted=False
        ).where(UserId=payload.Id))

        return await self._db_session.execute(stmt)

    async def get_data(self, user_id, category_id):
        stmt = (select(NetWorthUserTableData.AccountNumber,
                       NetWorthUserTableData.SchemeName,
                       NetWorthUserTableData.StartDate,
                       NetWorthUserTableData.SchemeType,
                       NetWorthUserTableData.Corpus,
                       NetWorthUserTableData.AnnuityIncome,
                       NetWorthUserTableData.GrowthOfPension,
                       NetWorthUserTableData.AnnuityMaturity,
                       NetWorthUserTableData.Frequency
                       ).where(UserId=user_id, CategoryID=category_id))

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data[0]

        return []

    async def get_all_data(self, user_id):
        stmt = (select(NetWorthUserTableData.AccountNumber,
                       NetWorthUserTableData.SchemeName,
                       NetWorthUserTableData.StartDate,
                       NetWorthUserTableData.SchemeType,
                       NetWorthUserTableData.Corpus,
                       NetWorthUserTableData.AnnuityIncome,
                       NetWorthUserTableData.GrowthOfPension,
                       NetWorthUserTableData.AnnuityMaturity,
                       NetWorthUserTableData.Frequency).where(UserId=user_id))

        result = await self._db_session.execute(stmt)

        result_data = []
        for data in result.fetchall():
            result_data.append(data)

        return result_data

    async def delete(self, user_id):
        stmt = (update(NetWorthUserTableData).values(
            IsDeleted=False
        ).where(UserId=user_id))

        return await self._db_session.execute(stmt)
