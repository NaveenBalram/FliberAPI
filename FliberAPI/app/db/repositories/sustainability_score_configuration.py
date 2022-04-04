from typing import Type

from uuid import UUID

from sqlalchemy import select

from app.db.errors import DoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.tables.sustainability_score_configuration import (
    SustainabilityScoreConfiguration,
)
from app.models.schema.sustainability_score_configuration import (
    SustainabilityScoreConfigurationSchemaBase,
    SustainabilityScoreConfigurationSchema,
    InSustainabilityScoreConfigurationSchema,
)


class SustainabilityScoreConfigurationRepository(
    BaseRepository[
        SustainabilityScoreConfigurationSchemaBase,
        SustainabilityScoreConfigurationSchema,
        SustainabilityScoreConfiguration,
    ]
):
    @property
    def _in_schema(self) -> Type[SustainabilityScoreConfigurationSchemaBase]:
        return InSustainabilityScoreConfigurationSchema

    @property
    def _schema(self) -> Type[SustainabilityScoreConfigurationSchema]:
        return SustainabilityScoreConfigurationSchema

    @property
    def _table(self) -> Type[SustainabilityScoreConfiguration]:
        return SustainabilityScoreConfiguration

    async def get_configurations(self):

        stmt = select(self._table)

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data

        raise DoesNotExist("Configuration data not available.")
