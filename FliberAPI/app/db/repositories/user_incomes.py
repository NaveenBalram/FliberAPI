from typing import Type

from sqlalchemy import and_
from sqlalchemy.future import select

from app.db.repositories.base import BaseRepository
from app.db.tables.frequency import Frequency
from app.db.tables.income_category import IncomeCategory
from app.db.tables.income_type import IncomeType
from app.db.tables.user_incomes import UserIncomes
from app.models.schema.user_incomes import (
    UserIncomesSchemaBase,
    UserIncomesSchema,
    InUserIncomesSchema,
)


class UserIncomesRepository(
    BaseRepository[UserIncomesSchemaBase, UserIncomesSchema, UserIncomes]
):
    @property
    def _in_schema(self) -> Type[UserIncomesSchemaBase]:
        return InUserIncomesSchema

    @property
    def _schema(self) -> Type[UserIncomesSchema]:
        return UserIncomesSchema

    @property
    def _table(self) -> Type[UserIncomes]:
        return UserIncomes

    async def fetch_user_income(self, user_id):
        """ method to fetch user income using user id"""
        print("user_income", user_id)
        stmt = (
            select(
                self._table.IncomeAmountType,
                self._table.IncomeAmount,
                self._table.IncomeInflationRate,
                self._table.IncomeStartAge,
                self._table.IncomeEndAge,
                self._table.IncomeFrequencyId,
                IncomeCategory.Name.label("IncomeCategoryName"),
                Frequency.Name.label("FrequencyName"),
                IncomeType.Name.label("IncomeTypeName"),
            )
                .join(IncomeType, IncomeType.Id == self._table.IncomeTypeId)
                .join(IncomeCategory, IncomeCategory.Id == self._table.IncomeCategoryId)
                .join(Frequency, Frequency.Id == self._table.IncomeFrequencyId)
                .where(and_(self._table.UserId == user_id, self._table.IsDeleted == False))
        )

        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            return_items.append(item)

        return return_items

    async def get_user_income_by_id(self, user_id):

        stmt = (
            select(self._table).where(and_(self._table.UserId == user_id, self._table.IsDeleted == False))
        )
        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            return_items.append(item[0].__dict__)
        return return_items
