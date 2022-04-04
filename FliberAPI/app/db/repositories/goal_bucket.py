from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.goal_bucket import GoalBucket
from app.models.schema.goal_bucket import (
    GoalBucketSchemaBase,
    GoalBucketSchema,
    InGoalBucketSchema,
)


class GoalBucketRepository(
    BaseRepository[GoalBucketSchemaBase, GoalBucketSchema, GoalBucket]
):
    @property
    def _in_schema(self) -> Type[GoalBucketSchemaBase]:
        return InGoalBucketSchema

    @property
    def _schema(self) -> Type[GoalBucketSchema]:
        return GoalBucketSchema

    @property
    def _table(self) -> Type[GoalBucket]:
        return GoalBucket
