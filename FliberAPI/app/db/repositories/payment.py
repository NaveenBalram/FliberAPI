from typing import Type

from sqlalchemy import select

from app.db.repositories.base import BaseRepository
from app.db.tables.payment import Payment
from app.models.schema.payment import PaymentSchemaBase, PaymentSchema, InPaymentSchema


class PaymentRepository(BaseRepository[PaymentSchemaBase, PaymentSchema, Payment]):
    @property
    def _in_schema(self) -> Type[PaymentSchemaBase]:
        return InPaymentSchema

    @property
    def _schema(self) -> Type[PaymentSchema]:
        return PaymentSchema

    @property
    def _table(self) -> Type[Payment]:
        return Payment

    async def get_by_payment_id(self, payment_id: int, order_id: str):
        stmt = select(self._table).where(
            self._table.cf_payment_id == payment_id, self._table.order_id == order_id
        )

        return_items = []
        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return_items.append(data[0])

        return return_items
