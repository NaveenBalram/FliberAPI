from typing import Type

from uuid import UUID

from sqlalchemy import select

from app.db.repositories.base import BaseRepository
from app.db.tables.sign_zy import SignZy
from app.models.schema.sign_zy import SignZySchemaBase, SignZySchema, InSignZySchema


class SignZyRepository(BaseRepository[SignZySchemaBase, SignZySchema, SignZy]):
    @property
    def _in_schema(self) -> Type[SignZySchemaBase]:
        return InSignZySchema

    @property
    def _schema(self) -> Type[SignZySchema]:
        return SignZySchema

    @property
    def _table(self) -> Type[SignZy]:
        return SignZy

    async def get_by_user_id(self, user_id: UUID):
        result = await self._db_session.execute(
            select(self._table).where(self._table.UserId == user_id)
        )
        return_items = []

        for item in result.fetchall():
            return_items.append(item[0])

        return return_items
