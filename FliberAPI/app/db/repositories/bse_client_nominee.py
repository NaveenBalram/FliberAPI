from typing import Type
from uuid import UUID

from sqlalchemy import delete, select

from app.db.repositories.base import BaseRepository
from app.db.tables.bse_client_nominee import BseClientNominee
from app.models.schema.bse_client_nominee import (
    BseClientNomineeSchemaBase,
    BseClientNomineeSchema,
    InBseClientNomineeSchema,
)


class BseClientNomineeRepository(
    BaseRepository[BseClientNomineeSchemaBase, BseClientNomineeSchema, BseClientNominee]
):
    @property
    def _in_schema(self) -> Type[BseClientNomineeSchemaBase]:
        return InBseClientNomineeSchema

    @property
    def _schema(self) -> Type[BseClientNomineeSchema]:
        return BseClientNomineeSchema

    @property
    def _table(self) -> Type[BseClientNominee]:
        return BseClientNominee

    async def delete_by_user_id(self, user_id: UUID):
        stmt = delete(self._table).where(self._table.UserId == user_id)

        await self._db_session.execute(stmt)

    async def check_exist(self, UserId, NomineeNumber):
        stmt = (
            select(self._table.NomineeNumber).where(self._table.UserId == UserId,
                                                        self._table.NomineeNumber == NomineeNumber)
        )

        result = await self._db_session.execute(stmt)

        result_item = []
        for data in result.fetchall():
            return data

        return result_item
