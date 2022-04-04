from typing import Type

from sqlalchemy import select, and_

from app.db.repositories.base import BaseRepository
from app.db.tables.willingness_configuration import WillingnessConfiguration
from app.models.schema.willingness_configuration import (
    WillingnessConfigurationSchemaBase,
    WillingnessConfigurationSchema,
    InWillingnessConfigurationSchema,
)


class WillingnessConfigurationRepository(
    BaseRepository[
        WillingnessConfigurationSchemaBase,
        WillingnessConfigurationSchema,
        WillingnessConfiguration,
    ]
):
    @property
    def _in_schema(self) -> Type[WillingnessConfigurationSchemaBase]:
        return InWillingnessConfigurationSchema

    @property
    def _schema(self) -> Type[WillingnessConfigurationSchema]:
        return WillingnessConfigurationSchema

    @property
    def _table(self) -> Type[WillingnessConfiguration]:
        return WillingnessConfiguration

    async def get_willingness_type(self, score: int):
        stmt = select(self._table.Type).where(
            and_(
                self._table.LowerLimit <= score,
                self._table.UpperLimit >= score,
                self._table.IsDeleted == False,
            )
        )

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        return []
