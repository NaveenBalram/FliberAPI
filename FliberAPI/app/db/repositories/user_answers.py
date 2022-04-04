from typing import Type

from sqlalchemy import func
from sqlalchemy.sql.expression import select

from app.db.errors import DoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.tables.user_answers import UserAnswers
from app.models.schema.user_answers import (
    UserAnswersSchemaBase,
    UserAnswersSchema,
    InUserAnswersSchema,
)


class UserAnswersRepository(
    BaseRepository[UserAnswersSchemaBase, UserAnswersSchema, UserAnswers]
):
    @property
    def _in_schema(self) -> Type[UserAnswersSchemaBase]:
        return InUserAnswersSchema

    @property
    def _schema(self) -> Type[UserAnswersSchema]:
        return UserAnswersSchema

    @property
    def _table(self) -> Type[UserAnswers]:
        return UserAnswers

    async def get_by_value(self, name):
        print(self._table)
        result = await self._db_session.execute(
            select(func.sum(self._table.S)).where(self._table.Name == name)
        )
        return_items = []
        for item in result.fetchall():
            return_items.append(item[0])
        if not return_items:
            raise DoesNotExist(f"Data does not exist")
        return return_items
