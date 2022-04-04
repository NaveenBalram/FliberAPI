from typing import Type
from uuid import UUID

from sqlalchemy import delete, update, select

from app.db.repositories.base import BaseRepository
from app.db.tables.bse_client_account import BseClientAccount
from app.models.schema.bse_client_account import (
    BseClientAccountSchemaBase,
    BseClientAccountSchema,
    InBseClientAccountSchema,
)


class BseClientAccountRepository(
    BaseRepository[BseClientAccountSchemaBase, BseClientAccountSchema, BseClientAccount]
):
    @property
    def _in_schema(self) -> Type[BseClientAccountSchemaBase]:
        return InBseClientAccountSchema

    @property
    def _schema(self) -> Type[BseClientAccountSchema]:
        return BseClientAccountSchema

    @property
    def _table(self) -> Type[BseClientAccount]:
        return BseClientAccount

    async def delete_by_user_id(self, user_id: UUID):
        stmt = delete(self._table).where(self._table.UserId == user_id)

        await self._db_session.execute(stmt)

    async def update_by_user(self, payload: BseClientAccountSchema):
        stmt = (
            update(self._table)
                .values(
                AccountTypeNumber=payload.AccountTypeNumber,
                AccountType=payload.AccountNo,
                MICRNo=payload.MICRNo,
                IFSCCode=payload.IFSCCode,
                DefaultBankFlag=payload.DefaultBankFlag,
                CreatedOn=payload.CreatedOn,
            )
                .where(self._table.UserId == payload.UserId)
        )

        await self._db_session.execute(stmt)

    async def check_exist(self, UserId, AccountTypeNumber):
        stmt = (
            select(self._table.AccountTypeNumber).where(self._table.UserId == UserId,
                                                        self._table.AccountTypeNumber == AccountTypeNumber)
        )

        result = await self._db_session.execute(stmt)

        result_item = []
        for data in result.fetchall():
            return data

        return result_item
