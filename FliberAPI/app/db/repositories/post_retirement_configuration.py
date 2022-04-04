from typing import Type

from sqlalchemy import select

from app.db.repositories.base import BaseRepository
from app.db.tables.post_retirement_configuration import PostRetirementConfiguration
from app.models.schema.post_retirement_configuration import (
    PostRetirementConfigurationSchemaBase,
    PostRetirementConfigurationSchema,
    InPostRetirementConfigurationSchema,
)


class PostRetirementConfigurationRepository(
    BaseRepository[
        PostRetirementConfigurationSchemaBase,
        PostRetirementConfigurationSchema,
        PostRetirementConfiguration,
    ]
):
    @property
    def _in_schema(self) -> Type[PostRetirementConfigurationSchemaBase]:
        return InPostRetirementConfigurationSchema

    @property
    def _schema(self) -> Type[PostRetirementConfigurationSchema]:
        return PostRetirementConfigurationSchema

    @property
    def _table(self) -> Type[PostRetirementConfiguration]:
        return PostRetirementConfiguration

    async def get_by_user(self, user_id):
        stmt = select(self._table)

        result = await self._db_session.execute(stmt)

        for data in result.fetchall():
            return data
