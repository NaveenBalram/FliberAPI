from typing import Type

from sqlalchemy import select

from app.db.repositories.base import BaseRepository
from app.db.tables.risk_profile_configuration import RiskProfileConfiguration
from app.models.schema.risk_profile_configuration import (
    RiskProfileConfigurationSchemaBase,
    RiskProfileConfigurationSchema,
    InRiskProfileConfigurationSchema,
)


class RiskProfileConfigurationRepository(
    BaseRepository[
        RiskProfileConfigurationSchemaBase,
        RiskProfileConfigurationSchema,
        RiskProfileConfiguration,
    ]
):
    @property
    def _in_schema(self) -> Type[RiskProfileConfigurationSchemaBase]:
        return InRiskProfileConfigurationSchema

    @property
    def _schema(self) -> Type[RiskProfileConfigurationSchema]:
        return RiskProfileConfigurationSchema

    @property
    def _table(self) -> Type[RiskProfileConfiguration]:
        return RiskProfileConfiguration

    async def get_risk_profile(self, ab_type):
        stmt = select(self._table).where(self._table.Type == ab_type)

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data
