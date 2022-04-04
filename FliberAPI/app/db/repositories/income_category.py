from typing import Type

from sqlalchemy.future import select

from app.db.errors import DoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.tables.income_category import IncomeCategory
from app.models.schema.income_category import (
    IncomeCategorySchemaBase,
    IncomeCategorySchema,
    InIncomeCategorySchema,
)


class IncomeCategoryRepository(
    BaseRepository[IncomeCategorySchemaBase, IncomeCategorySchema, IncomeCategory]
):
    @property
    def _in_schema(self) -> Type[IncomeCategorySchemaBase]:
        return InIncomeCategorySchema

    @property
    def _schema(self) -> Type[IncomeCategorySchema]:
        return IncomeCategorySchema

    @property
    def _table(self) -> Type[IncomeCategory]:
        return IncomeCategory

    async def get_by_name(self, kwargs):
        result = await self._db_session.execute(
            select(self._table.Rate).where(self._table.Name == kwargs["Name"])
        )

        return_items = []
        for item in result.fetchall():
            return_items.append(item[0])
        if not return_items:
            raise DoesNotExist(f"Income data does not exist")
        return return_items
