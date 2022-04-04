from typing import Type

from sqlalchemy.sql.expression import select, and_

from app.db.errors import DoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.tables.question import Question
from app.db.tables.question_type import QuestionType
from app.models.schema.question_type import (
    QuestionTypeSchemaBase,
    QuestionTypeSchema,
    InQuestionTypeSchema,
)


class QuestionTypeRepository(
    BaseRepository[QuestionTypeSchemaBase, QuestionTypeSchema, QuestionType]
):
    @property
    def _in_schema(self) -> Type[QuestionTypeSchemaBase]:
        return InQuestionTypeSchema

    @property
    def _schema(self) -> Type[QuestionTypeSchema]:
        return QuestionTypeSchema

    @property
    def _table(self) -> Type[QuestionType]:
        return QuestionType

    async def get_by_name(self, name):

        result = await self._db_session.execute(
            select(self._table.Id).where(self._table.Name == name)
        )
        return_items = []
        for item in result.fetchall():
            return_items.append(item[0])
        if not return_items:
            raise DoesNotExist(f"Data does not exist")
        return return_items

    async def get_by_type(self, module_type: int):

        if module_type == 1:
            result = await self._db_session.execute(
                select(self._table).where(self._table.Name == "RRScore")
            )
            rid = None

            for item in result.fetchall():
                rid = item[0].Id

            stmt = select(Question).where(Question.QuestionTypeId == rid)
            result = await self._db_session.execute(stmt)

            result_items = []
            for item in result.fetchall():
                result_items.append(item[0].__dict__)

            return result_items

        if module_type == 2:
            ability = await self._db_session.execute(
                select(self._table).where(
                    and_(self._table.Name == "Ability", self._table.IsDeleted == False)
                )
            )
            aid = None
            for item in ability.fetchall():
                aid = item[0].Id
            willingness = await self._db_session.execute(
                select(self._table).where(
                    and_(
                        self._table.Name == "Willingness",
                        self._table.IsDeleted == False,
                    )
                )
            )
            wid = None
            for item in willingness.fetchall():
                wid = item[0].Id

            questions = await self._db_session.execute(
                select(Question)
                .join_from(self._table, Question)
                .where(
                    and_(Question.QuestionTypeId == aid, self._table.IsDeleted == False)
                )
            )

            result_items = []
            for item in questions.fetchall():
                result_items.append(item[0].__dict__)

            questions = await self._db_session.execute(
                select(Question)
                .join_from(self._table, Question)
                .where(
                    and_(Question.QuestionTypeId == wid, self._table.IsDeleted == False)
                )
            )

            for item in questions.fetchall():
                result_items.append(item[0].__dict__)

            return result_items

        if module_type == 3:
            result = await self._db_session.execute(
                select(self._table).where(self._table.Name == "Sustainability Score")
            )
            rid = None

            for item in result.fetchall():
                rid = item[0].Id

            stmt = select(Question).where(
                and_(Question.QuestionTypeId == rid, Question.IsDeleted == False)
            )
            result = await self._db_session.execute(stmt)

            result_items = []
            for item in result.fetchall():
                result_items.append(item[0].__dict__)

            return result_items
