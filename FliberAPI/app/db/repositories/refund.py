from typing import Type
from uuid import UUID

from sqlalchemy import select

from app.db.repositories.base import BaseRepository
from app.db.tables.refund import Refund
from app.models.schema.refund import RefundSchemaBase, RefundSchema, InRefundSchema


class RefundRepository(BaseRepository[RefundSchemaBase, RefundSchema, Refund]):
    @property
    def _in_schema(self) -> Type[RefundSchemaBase]:
        return InRefundSchema

    @property
    def _schema(self) -> Type[RefundSchema]:
        return RefundSchema

    @property
    def _table(self) -> Type[Refund]:
        return Refund

    async def get_refund(self, user_id: UUID):
        stmt = select(self._table).where(self._table.user_id == user_id)

        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            return_items.append(item[0].__dict__)

        return return_items

    async def get_by_order_id(self, order_id):
        stmt = select(self._table).where(self._table.order_id == order_id)

        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            return_items.append(item[0].__dict__)

        return return_items

    async def get_by_payment_id(self, order_id: str, payment_id: str):
        stmt = select(self._table).where(
            self._table.order_id == order_id, self._table.cf_payment_id == payment_id
        )

        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            return_items.append(item[0].__dict__)

        return return_items
