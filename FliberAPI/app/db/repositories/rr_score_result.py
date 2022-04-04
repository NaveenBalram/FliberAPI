from typing import Type

from sqlalchemy import delete

from app.db.repositories.base import BaseRepository
from app.db.tables.rr_score_result import RrScoreResult
from app.models.schema.rr_score_result import RrScoreResultSchemaBase, RrScoreResultSchema, InRrScoreResultSchema


class RrScoreResultRepository(BaseRepository[RrScoreResultSchemaBase, RrScoreResultSchema, RrScoreResult]):
    @property
    def _in_schema(self) -> Type[RrScoreResultSchemaBase]:
        return InRrScoreResultSchema

    @property
    def _schema(self) -> Type[RrScoreResultSchema]:
        return RrScoreResultSchema

    @property
    def _table(self) -> Type[RrScoreResult]:
        return RrScoreResult

    async def delete_by_user(self, user_id):
        await self._db_session.execute(delete(self._table).where(self._table.UserId == user_id))
