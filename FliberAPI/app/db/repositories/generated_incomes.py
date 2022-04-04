from typing import Type

from sqlalchemy import delete

from app.db.repositories.base import BaseRepository
from app.db.tables.generated_incomes import GeneratedIncomes
from app.models.schema.generated_incomes import (
    GeneratedIncomesSchemaBase,
    GeneratedIncomesSchema,
    InGeneratedIncomesSchema,
)


class GeneratedIncomesRepository(
    BaseRepository[GeneratedIncomesSchemaBase, GeneratedIncomesSchema, GeneratedIncomes]
):
    @property
    def _in_schema(self) -> Type[GeneratedIncomesSchemaBase]:
        return InGeneratedIncomesSchema

    @property
    def _schema(self) -> Type[GeneratedIncomesSchema]:
        return GeneratedIncomesSchema

    @property
    def _table(self) -> Type[GeneratedIncomes]:
        return GeneratedIncomes

    async def delet_incomes_by_user_id(self, user_id):
        return await self._db_session.execute(delete(self._table).where(self._table.UserId == user_id))