from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.payment_type import PaymentType
from app.models.schema.payment_type import (
    PaymentTypeSchemaBase,
    PaymentTypeSchema,
    InPaymentTypeSchema,
)


class PaymentTypeRepository(
    BaseRepository[PaymentTypeSchemaBase, PaymentTypeSchema, PaymentType]
):
    @property
    def _in_schema(self) -> Type[PaymentTypeSchemaBase]:
        return InPaymentTypeSchema

    @property
    def _schema(self) -> Type[PaymentTypeSchema]:
        return PaymentTypeSchema

    @property
    def _table(self) -> Type[PaymentType]:
        return PaymentType
