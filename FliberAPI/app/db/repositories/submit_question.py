import uuid
from typing import Type

from sqlalchemy import func
from sqlalchemy.sql.expression import select, insert, delete

from app.db.repositories.base import BaseRepository
from app.db.tables.question import Question
from app.db.tables.submit_question import SubmitQuestion
from app.models.schema.submit_question import (
    SubmitQuestionSchemaBase,
    SubmitQuestionSchema,
    InSubmitQuestionSchema,
)


class SubmitQuestionRepository(
    BaseRepository[SubmitQuestionSchemaBase, SubmitQuestionSchema, SubmitQuestion]
):
    @property
    def _in_schema(self) -> Type[SubmitQuestionSchemaBase]:
        return InSubmitQuestionSchema

    @property
    def _schema(self) -> Type[SubmitQuestionSchema]:
        return SubmitQuestionSchema

    @property
    def _table(self) -> Type[SubmitQuestion]:
        return SubmitQuestion

    async def get_by_value(self, kwargs):

        if kwargs["ModuleType"] == 1 or kwargs["ModuleType"] == 3:
            result = await self._db_session.execute(
                select(self._table.UserText).where(
                    self._table.QuestionId == kwargs["QuestionId"],
                    self._table.UserId == kwargs["UserId"],
                    self._table.ModuleType == kwargs["ModuleType"],
                )
            )
        else:
            result = await self._db_session.execute(
                select(func.sum(self._table.SelectedValue))
                    .join_from(self._table, Question)
                    .where(
                    Question.QuestionTypeId == kwargs["QuestionId"],
                    self._table.UserId == kwargs["UserId"],
                    self._table.ModuleType == kwargs["ModuleType"],
                )
            )

        return_items = []
        for item in result.fetchall():
            return_items.append(item[0])
        return return_items

    async def bulk_create(self, payload: list[SubmitQuestionSchemaBase]):
        result = []
        flag = True
        for data in payload:
            if flag:
                stmt = (delete(self._table).where(self._table.UserId == data.UserId,
                                                  self._table.ModuleType == data.ModuleType))
                await self._db_session.execute(stmt)
                await self._db_session.commit()
                flag = False

            data = data.__dict__
            data["Id"] = uuid.uuid4()
            result.append(data)

        await self._db_session.execute(insert(self._table).values(result))
        await self._db_session.commit()
        return result
