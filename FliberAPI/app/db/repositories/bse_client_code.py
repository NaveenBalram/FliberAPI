from typing import Type
from uuid import UUID

from sqlalchemy import update
from sqlalchemy.future import select

from app.db.repositories.base import BaseRepository
from app.db.tables.bse_client_account import BseClientAccount
from app.db.tables.bse_client_code import BseClientCode
from app.db.tables.bse_client_nominee import BseClientNominee
from app.models.schema.bse_client_code import (
    BseClientCodeSchemaBase,
    BseClientCodeSchema,
    InBseClientCodeSchema,
)
from app.models.schema.bse_client_code_screen_two import (
    BseClientCodeScreenFour,
    BseClientCodeScreenTwo,
    BseClientCodeScreenThree,
)


class BseClientCodeRepository(
    BaseRepository[BseClientCodeSchemaBase, BseClientCodeSchema, BseClientCode]
):
    @property
    def _in_schema(self) -> Type[BseClientCodeSchemaBase]:
        return InBseClientCodeSchema

    @property
    def _schema(self) -> Type[BseClientCodeSchema]:
        return BseClientCodeSchema

    @property
    def _table(self) -> Type[BseClientCode]:
        return BseClientCode

    async def get_bse_user(self, user_id: UUID):
        stmt = select(self._table).where(self._table.UserId == user_id)

        nominee_stmt = select(BseClientNominee).where(
            BseClientNominee.UserId == user_id
        )
        nomine = await self._db_session.execute(nominee_stmt)

        nominees = []
        for item in nomine.fetchall():
            nominees.append(item[0].__dict__)

        account_stmt = select(BseClientAccount).where(
            BseClientAccount.UserId == user_id
        )
        account = await self._db_session.execute(account_stmt)

        accounts = []
        for item in account.fetchall():
            accounts.append(item[0].__dict__)

        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            item = dict(item[0].__dict__)
            item["BseNominees"] = nominees
            item["BseAccount"] = accounts
            return_items.append(item)

        return return_items

    async def find_by_user_id(self, user_id: UUID):

        stmt = select(self._table).where(self._table.UserId == user_id)

        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            return_items.append(item)
        return return_items

    async def update_screen_two(self, payload: BseClientCodeScreenTwo):
        stmt = (
            update(self._table)
            .values(OccupationCode=payload.OccupationCode)
            .where(self._table.UserId == payload.UserId)
        )

        await self._db_session.execute(stmt)

    async def get_screen_two(self, user_id: UUID):
        stmt = select(self._table.OccupationCode).where(self._table.UserId == user_id)
        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            return_items.append(item)
        return return_items

    async def update_screen_three(self, payload: BseClientCodeScreenThree):
        stmt = update(self._table).values(
            AddressOne=payload.AddressOne,
            AddressTwo=payload.AddressTwo,
            City=payload.CityCode,
            State=payload.StateCode,
            PinCode=payload.PinCode,
        )
        await self._db_session.execute(stmt)

    async def get_screen_three(self, user_id: UUID):
        stmt = select(
            self._table.AddressOne,
            self._table.AddressTwo,
            self._table.City,
            self._table.State,
            self._table.PinCode,
        ).where(self._table.UserId == user_id)
        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            return_items.append(item)
        return return_items

    async def update_signature(self, signature: BseClientCodeScreenFour):
        try:
            stmt = (
                update(self._table)
                .values(UserId=signature.UserId, SignatureUrl=signature.SignatureUrl)
                .where(self._table.UserId == signature.UserId)
            )

            await self._db_session.execute(stmt)
        except Exception as e:
            return f"Update Failed: {e}"
