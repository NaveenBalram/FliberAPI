from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.goal_type import GoalType
from app.models.schema.goal_type import (
    GoalTypeSchemaBase,
    GoalTypeSchema,
    InGoalTypeSchema,
)


class GoalTypeRepository(BaseRepository[GoalTypeSchemaBase, GoalTypeSchema, GoalType]):
    @property
    def _in_schema(self) -> Type[GoalTypeSchemaBase]:
        return InGoalTypeSchema

    @property
    def _schema(self) -> Type[GoalTypeSchema]:
        return GoalTypeSchema

    @property
    def _table(self) -> Type[GoalType]:
        return GoalType
