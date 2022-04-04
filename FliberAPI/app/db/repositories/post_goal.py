from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.post_goal import PostGoal
from app.models.schema.post_goal import (
    PostGoalSchemaBase,
    PostGoalSchema,
    InPostGoalSchema,
)


class PostGoalRepository(BaseRepository[PostGoalSchemaBase, PostGoalSchema, PostGoal]):
    @property
    def _in_schema(self) -> Type[PostGoalSchemaBase]:
        return InPostGoalSchema

    @property
    def _schema(self) -> Type[PostGoalSchema]:
        return PostGoalSchema

    @property
    def _table(self) -> Type[PostGoal]:
        return PostGoal
