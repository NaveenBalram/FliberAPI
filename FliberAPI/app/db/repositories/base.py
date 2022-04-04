import abc
from typing import Generic, TypeVar, Type
from uuid import uuid4, UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select, update, and_

from app.models.schema.base import BaseSchema

IN_SCHEMA = TypeVar("IN_SCHEMA", bound=BaseSchema)
SCHEMA = TypeVar("SCHEMA", bound=BaseSchema)
TABLE = TypeVar("TABLE")


class BaseRepository(Generic[IN_SCHEMA, SCHEMA, TABLE], metaclass=abc.ABCMeta):
    def __init__(self, db_session: AsyncSession, *args, **kwargs) -> None:
        self._db_session: AsyncSession = db_session

    @property
    @abc.abstractmethod
    def _table(self) -> Type[TABLE]:
        ...

    @property
    @abc.abstractmethod
    def _schema(self) -> Type[SCHEMA]:
        ...

    async def create(self, in_schema: IN_SCHEMA) -> SCHEMA:
        entry = self._table(Id=uuid4(), **in_schema.dict())
        self._db_session.add(entry)
        await self._db_session.commit()
        return self._schema.from_orm(entry)

    async def get_by_id(self, entry_id: UUID):

        result = await self._db_session.execute(
            select(self._table).where(
                and_(self._table.Id == entry_id, self._table.IsDeleted == False)
            )
        )

        for item in result.fetchall():
            return item[0].__dict__

    async def get_all(self):
        result = await self._db_session.execute(
            select(self._table).where(self._table.IsDeleted == False)
        )

        return_items = []
        for item in result.fetchall():
            return_items.append(item[0].__dict__)
        return return_items

    async def delete(self, entry_id: UUID):
        await self._db_session.execute(
            update(self._table).values(IsDeleted=True).where(self._table.Id == entry_id)
        )
        return "Deleted!"

    async def delete_by_user_id(self, entry_id: UUID):
        await self._db_session.execute(
            update(self._table)
                .values(IsDeleted=True)
                .where(self._table.UserId == entry_id)
        )
        return "Deleted!"

    async def update(self, in_schema: SCHEMA):
        await self._db_session.execute(
            update(self._table)
                .where(self._table.Id == in_schema.Id)
                .values(**in_schema.dict())
        )
        return "Updated!"

    async def get_by_user_id(self, entry_id: UUID):

        result = await self._db_session.execute(
            select(self._table).where(
                and_(self._table.UserId == entry_id, self._table.IsDeleted == False)
            )
        )

        return_item = []
        for item in result.fetchall():
            return item[0].__dict__

        return return_item
