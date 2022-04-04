from typing import Type

from sqlalchemy.future import select

from app.db.errors import DoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.tables.goal_category import GoalCategory
from app.models.schema.goal_category import (
    GoalCategorySchemaBase,
    GoalCategorySchema,
    InGoalCategorySchema,
)


class GoalCategoryRepository(
    BaseRepository[GoalCategorySchemaBase, GoalCategorySchema, GoalCategory]
):
    @property
    def _in_schema(self) -> Type[GoalCategorySchemaBase]:
        return InGoalCategorySchema

    @property
    def _schema(self) -> Type[GoalCategorySchema]:
        return GoalCategorySchema

    @property
    def _table(self) -> Type[GoalCategory]:
        return GoalCategory

    async def get_by_name(self, kwargs):
        result = await self._db_session.execute(
            select(self._table.Rate).where(self._table.Name == kwargs["Name"])
        )

        return_items = []
        for item in result.fetchall():
            return_items.append(item[0])
        if not return_items:
            raise DoesNotExist(f"Data does not exist")
        return return_items
