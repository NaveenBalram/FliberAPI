from typing import Type

from sqlalchemy import select, and_


from app.db.repositories.base import BaseRepository
from app.db.tables.ability_configuration import AbilityConfiguration
from app.models.schema.ability_configuration import (
    AbilityConfigurationSchemaBase,
    AbilityConfigurationSchema,
    InAbilityConfigurationSchema,
)


class AbilityConfigurationRepository(
    BaseRepository[
        AbilityConfigurationSchemaBase, AbilityConfigurationSchema, AbilityConfiguration
    ]
):
    @property
    def _in_schema(self) -> Type[AbilityConfigurationSchemaBase]:
        return InAbilityConfigurationSchema

    @property
    def _schema(self) -> Type[AbilityConfigurationSchema]:
        return AbilityConfigurationSchema

    @property
    def _table(self) -> Type[AbilityConfiguration]:
        return AbilityConfiguration

    async def get_ability_type(self, score: int):
        stmt = select(self._table.Type).where(
            (self._table.LowerLimit <= score) & (self._table.UpperLimit >= score)
        )

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data
