from typing import Type

from sqlalchemy import delete

from app.db.repositories.base import BaseRepository
from app.db.tables.generated_cash_ladder import GeneratedCashLadder
from app.models.schema.generated_cash_ladder import (
    GeneratedCashLadderSchemaBase,
    GeneratedCashLadderSchema,
    InGeneratedCashLadderSchema,
)


class GeneratedCashLadderRepository(
    BaseRepository[
        GeneratedCashLadderSchemaBase, GeneratedCashLadderSchema, GeneratedCashLadder
    ]
):
    @property
    def _in_schema(self) -> Type[GeneratedCashLadderSchemaBase]:
        return InGeneratedCashLadderSchema

    @property
    def _schema(self) -> Type[GeneratedCashLadderSchema]:
        return GeneratedCashLadderSchema

    @property
    def _table(self) -> Type[GeneratedCashLadder]:
        return GeneratedCashLadder

    async def delete_cash_ladder_by_user_id(self, user_id):
       return await self._db_session.execute(delete(self._table).where(self._table.UserId==user_id))
