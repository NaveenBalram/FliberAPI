from typing import Type
from uuid import UUID

from sqlalchemy import and_
from sqlalchemy.future import select

from app.db.repositories.base import BaseRepository
from app.db.tables.frequency import Frequency
from app.db.tables.goal_category import GoalCategory
from app.db.tables.goal_type import GoalType
from app.db.tables.user_goals import UserGoals
from app.models.schema.user_goals import (
    UserGoalsSchemaBase,
    UserGoalsSchema,
    InUserGoalsSchema
)


class UserGoalsRepository(
    BaseRepository[UserGoalsSchemaBase, UserGoalsSchema, UserGoals]
):
    @property
    def _in_schema(self) -> Type[UserGoalsSchemaBase]:
        return InUserGoalsSchema

    @property
    def _schema(self) -> Type[UserGoalsSchema]:
        return UserGoalsSchema

    @property
    def _table(self) -> Type[UserGoals]:
        return UserGoals

    async def fetch_user_goals(self, user_id: UUID):
        """ method to fetch saved user goals using user id. """

        stmt = (
            select(
                self._table.GoalName,
                self._table.GoalAmount,
                self._table.GoalPriority,
                self._table.GoalInflationRate,
                self._table.GoalStartAge,
                self._table.GoalEndAge,
                self._table.GoalAmountType,
                GoalCategory.Name.label("GoalCategoryName"),
                Frequency.Name.label("FrequencyName"),
                GoalType.Name.label("GoalTypeName"),

            ).join(GoalCategory, self._table.GoalCategoryId == GoalCategory.Id)
                .join(GoalType, self._table.GoalTypeId == GoalType.Id)
                .join(Frequency, self._table.GoalFrequencyId == Frequency.Id)
                .where(and_(self._table.UserId == user_id, self._table.IsDeleted == False)))

        result = await self._db_session.execute(stmt)

        return_items = []
        return_goals = []
        for item in result.fetchall():
            data = dict(item)
            return_goals.append(data)
            return_items.append(item)

        return return_items, return_goals

    async def get_user_goal_by_id(self, user_id):
        stmt = (
            select(self._table).where(and_(self._table.UserId == user_id, self._table.IsDeleted == False))
        )
        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            return_items.append(item[0].__dict__)
        return return_items
