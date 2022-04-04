from typing import Type
from uuid import UUID

from sqlalchemy import select

from app.db.errors import DoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.tables.signzy_users import SignzyUsers
from app.models.schema.signzy_users import (
    SignzyUsersSchemaBase,
    SignzyUsersSchema,
    InSignzyUsersSchema,
)


class SignzyUsersRepository(
    BaseRepository[SignzyUsersSchemaBase, SignzyUsersSchema, SignzyUsers]
):
    @property
    def _in_schema(self) -> Type[SignzyUsersSchemaBase]:
        return InSignzyUsersSchema

    @property
    def _schema(self) -> Type[SignzyUsersSchema]:
        return SignzyUsersSchema

    @property
    def _table(self) -> Type[SignzyUsers]:
        return SignzyUsers

    async def get_by_user_id(self, user_id: UUID):
        result = await self._db_session.execute(
            select(self._table).where(self._table.UserId == user_id)
        )
        return_items = []

        for item in result.fetchall():
            print("item", item)
            return_items.append(item[0])

        return return_items
