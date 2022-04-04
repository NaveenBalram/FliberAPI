import uuid
from typing import Type
from uuid import UUID

from sqlalchemy import select, and_, update, insert

from app.db.repositories.base import BaseRepository
from app.db.tables.users_re_balance_sheet import UsersReBalanceSheet
from app.models.schema.users_re_balance_sheet import (
    UsersReBalanceSheetSchemaBase,
    UsersReBalanceSheetSchema,
    InUsersReBalanceSheetSchema,
)


class UsersReBalanceSheetRepository(
    BaseRepository[
        UsersReBalanceSheetSchemaBase, UsersReBalanceSheetSchema, UsersReBalanceSheet
    ]
):
    @property
    def _in_schema(self) -> Type[UsersReBalanceSheetSchemaBase]:
        return InUsersReBalanceSheetSchema

    @property
    def _schema(self) -> Type[UsersReBalanceSheetSchema]:
        return UsersReBalanceSheetSchema

    @property
    def _table(self) -> Type[UsersReBalanceSheet]:
        return UsersReBalanceSheet

    async def get_all_by_status(self, user_id: None):
        if user_id:
            query = and_(
                self._table.IsDeleted == False,
                self._table.TransactionStatus != "InProgress",
                self._table.ReBalanceStatus != "InProgress",
                self._table.UserId == user_id,
            )
        else:
            query = and_(
                self._table.IsDeleted == False,
                self._table.TransactionStatus != "InProgress",
                self._table.ReBalanceStatus != "InProgress",
            )

        stmt = select(self._table).where(query)

        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            if user_id:
                return item[0].__dict__
            return_items.append(item[0].__dict__)
        await self._db_session.commit()
        return return_items

    async def update_target_id(self, target_id: UUID, user_id: UUID):
        print("target :", target_id)
        print("user_id: ", user_id)
        stmt = (update(self._table).values(TargetAssetsId=target_id)).where(
            self._table.UserId == user_id
        )
        await self._db_session.execute(stmt)
        await self._db_session.commit()

    async def update_watch_day(self, user_id: UUID, day: int, date):
        stmt = (update(self._table).values(WatchDays=day, UpdatedOn=date)).where(
            self._table.UserId == user_id
        )
        await self._db_session.execute(stmt)
        await self._db_session.commit()

    async def set_status(self, user_id: UUID, status: str, date):
        stmt = (update(self._table).values(ReBalanceStatus=status, UpdatedOn=date)).where(
            self._table.UserId == user_id
        )
        await self._db_session.execute(stmt)
        await self._db_session.commit()

    async def bulk_create(self, payload: list[UsersReBalanceSheet]):
        result = []
        for data in payload:
            data = data.__dict__
            data["Id"] = uuid.uuid4()
            result.append(data)

        await self._db_session.execute(insert(self._table).values(result))
        await self._db_session.commit()
        return result

    async def update_rebalance_sheet(self, payload, user_id):

        stmt = (
            update(self._table)
            .where(self._table.UserId == user_id)
            .values(Amount=payload.Amount)
        )

        await self._db_session.execute(stmt)
        await self._db_session.commit()

    async def update_sip_rebalance_sheet(self, payload, user_id):

        stmt = (
            update(self._table)
            .where(self._table.UserId == user_id)
            .values(
                Amount=payload.Amount,
                SIPAmount=payload.SIPAmount,
                SIPAccount=payload.SIPAccount,
            )
        )

        await self._db_session.execute(stmt)
        await self._db_session.commit()

    # async def create_or_update(self, payload, user_id):
