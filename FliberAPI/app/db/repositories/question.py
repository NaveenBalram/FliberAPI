from typing import Type

from sqlalchemy.future import select

from app.db.errors import DoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.tables.question import Question
from app.db.tables.question_type import QuestionType
from app.models.schema.question import (
    QuestionSchemaBase,
    QuestionSchema,
    InQuestionSchema,
)


class QuestionRepository(BaseRepository[QuestionSchemaBase, QuestionSchema, Question]):
    @property
    def _in_schema(self) -> Type[QuestionSchemaBase]:
        return InQuestionSchema

    @property
    def _schema(self) -> Type[QuestionSchema]:
        return QuestionSchema

    @property
    def _table(self) -> Type[Question]:
        return Question

    async def question_info(self, ref_id1: int, ref_id2: int):
        if ref_id2:
            result = await self._db_session.execute(
                select(self._table).where(
                    self._table.Ref_Id == ref_id1, self._table.Ref_Id == ref_id2
                )
            )
        else:
            result = await self._db_session.execute(
                select(self._table).where(self._table.Ref_Id == ref_id1)
            )

        return_items = []
        for item in result.fetchall():
            return_items.append(item)
        if not return_items:
            raise DoesNotExist(f"Data does not exist")
        return return_items

    async def test_key(self):
        result = await self._db_session.execute(
            select(self._table.QuestionTitle, QuestionType.Name)
                .join_from(self._table, QuestionType)
                .where(self._table.Id == "d27c6745-092b-4bc0-91ba-d209d4c91e85")
        )

        return_items = []
        for item in result.fetchall():
            return_items.append(item)
        if not return_items:
            raise DoesNotExist(f"Data does not exist")
        return return_items

    async def get_by_question_type(self, question_type):

        result = await self._db_session.execute(
            select(self._table.Id, self._table.QuestionSequence)
                .where(self._table.QuestionTypeId == question_type)
        )

        return_items = []
        for item in result.fetchall():
            return_items.append(item)
        if not return_items:
            raise DoesNotExist(f"Question Data does not exist for id {question_type}.")
        return return_items
