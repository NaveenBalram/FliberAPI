from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.pre_retirement_configuration import PreRetirementConfiguration
from app.models.schema.pre_retirement_configuration import (
    PreRetirementConfigurationSchemaBase,
    PreRetirementConfigurationSchema,
    InPreRetirementConfigurationSchema,
)


class PreRetirementConfigurationRepository(
    BaseRepository[
        PreRetirementConfigurationSchemaBase,
        PreRetirementConfigurationSchema,
        PreRetirementConfiguration,
    ]
):
    @property
    def _in_schema(self) -> Type[PreRetirementConfigurationSchemaBase]:
        return InPreRetirementConfigurationSchema

    @property
    def _schema(self) -> Type[PreRetirementConfigurationSchema]:
        return PreRetirementConfigurationSchema

    @property
    def _table(self) -> Type[PreRetirementConfiguration]:
        return PreRetirementConfiguration
