from typing import Type

from uuid import UUID

from sqlalchemy import select, delete

from app.db.repositories.base import BaseRepository
from app.db.tables.rr_score_configuration import RrScoreConfiguration
from app.models.schema.rr_score_configuration import (
    RrScoreConfigurationSchemaBase,
    RrScoreConfigurationSchema,
    InRrScoreConfigurationSchema,
)


class RrScoreConfigurationRepository(
    BaseRepository[
        RrScoreConfigurationSchemaBase, RrScoreConfigurationSchema, RrScoreConfiguration
    ]
):
    @property
    def _in_schema(self) -> Type[RrScoreConfigurationSchemaBase]:
        return InRrScoreConfigurationSchema

    @property
    def _schema(self) -> Type[RrScoreConfigurationSchema]:
        return RrScoreConfigurationSchema

    @property
    def _table(self) -> Type[RrScoreConfiguration]:
        return RrScoreConfiguration

    async def get_configurations(self):
        stmt = select(self._table)

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data




