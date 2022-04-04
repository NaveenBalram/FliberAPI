from typing import Type
from uuid import UUID

from sqlalchemy.future import select

from app.db.repositories.base import BaseRepository
from app.db.tables.choice import Choice
from app.models.schema.choice import ChoiceSchemaBase, ChoiceSchema, InChoiceSchema


class ChoiceRepository(BaseRepository[ChoiceSchemaBase, ChoiceSchema, Choice]):
    @property
    def _in_schema(self) -> Type[ChoiceSchemaBase]:
        return InChoiceSchema

    @property
    def _schema(self) -> Type[ChoiceSchema]:
        return ChoiceSchema

    @property
    def _table(self) -> Type[Choice]:
        return Choice

    async def get_by_question_id(self, question_id: UUID):
        result = await self._db_session.execute(
            select(
                self._table.Id,
                self._table.Text,
                self._table.Value,
                self._table.Ref_Id,
                self._table.ChoiceSequence,
            ).where(self._table.QuestionId == question_id)
        )

        return_items = []
        for item in result.fetchall():
            return_items.append(item)
        return return_items
