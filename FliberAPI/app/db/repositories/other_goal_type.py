from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.other_goal_type import OtherGoalType
from app.models.schema.other_goal_type import (
    OtherGoalTypeSchemaBase,
    OtherGoalTypeSchema,
    InOtherGoalTypeSchema,
)


class OtherGoalTypeRepository(
    BaseRepository[OtherGoalTypeSchemaBase, OtherGoalTypeSchema, OtherGoalType]
):
    @property
    def _in_schema(self) -> Type[OtherGoalTypeSchemaBase]:
        return InOtherGoalTypeSchema

    @property
    def _schema(self) -> Type[OtherGoalTypeSchema]:
        return OtherGoalTypeSchema

    @property
    def _table(self) -> Type[OtherGoalType]:
        return OtherGoalType
