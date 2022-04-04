from typing import Type
from uuid import uuid4

from sqlalchemy import insert, update

from app.db.repositories.base import BaseRepository
from app.db.tables.order import Order
from app.models.schema.order import OrderSchemaBase, OrderSchema, InOrderSchema


class OrderRepository(BaseRepository[OrderSchemaBase, OrderSchema, Order]):
    @property
    def _in_schema(self) -> Type[OrderSchemaBase]:
        return InOrderSchema

    @property
    def _schema(self) -> Type[OrderSchema]:
        return OrderSchema

    @property
    def _table(self) -> Type[Order]:
        return Order

    async def generate(self, orders: OrderSchemaBase):
        stmt = insert(self._table).values(Id=uuid4(), **orders.dict())

        await self._db_session.execute(stmt)

        return orders

    async def update_by_token(self, token: str, payment_id: str, method: str):
        stmt = (
            update(self._table)
            .values(CFPaymentId=payment_id, PaymentMethod=method)
            .where(self._table.OrderToken == token)
        )

        await self._db_session.execute(stmt)
