from typing import Type

import uuid

from sqlalchemy import insert, delete

from app.db.repositories.base import BaseRepository
from app.db.tables.generated_goals import GeneratedGoals
from app.models.schema.generated_goals import (
    GeneratedGoalsSchemaBase,
    GeneratedGoalsSchema,
    InGeneratedGoalsSchema,
)


class GeneratedGoalsRepository(
    BaseRepository[GeneratedGoalsSchemaBase, GeneratedGoalsSchema, GeneratedGoals]
):
    @property
    def _in_schema(self) -> Type[GeneratedGoalsSchemaBase]:
        return InGeneratedGoalsSchema

    @property
    def _schema(self) -> Type[GeneratedGoalsSchema]:
        return GeneratedGoalsSchema

    @property
    def _table(self) -> Type[GeneratedGoals]:
        return GeneratedGoals

    async def bulk_insert(self, payload: list[GeneratedGoalsSchemaBase]):
        result = []
        for data in payload:
            data = data.__dict__
            data["Id"] = uuid.uuid4()
            result.append(data)

        await self._db_session.execute(insert(self._table).values(result))
        await self._db_session.commit()
        return result

    async def delete_goals_by_user_id(self, user_id):
        return await self._db_session.execute(delete(self._table).where(self._table.UserId==user_id))
