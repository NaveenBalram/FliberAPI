from typing import Type
from uuid import UUID

from sqlalchemy.future import select

from app.db.errors import DoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.tables.retirement_status import RetirementStatus
from app.db.tables.user import User
from app.models.schema.retirement_status import (
    RetirementStatusSchemaBase,
    RetirementStatusSchema,
    InRetirementStatusSchema,
)


class RetirementStatusRepository(
    BaseRepository[RetirementStatusSchemaBase, RetirementStatusSchema, RetirementStatus]
):
    @property
    def _in_schema(self) -> Type[RetirementStatusSchemaBase]:
        return InRetirementStatusSchema

    @property
    def _schema(self) -> Type[RetirementStatusSchema]:
        return RetirementStatusSchema

    @property
    def _table(self) -> Type[RetirementStatus]:
        return RetirementStatus

    async def get_status(self, user_id: UUID):
        result = await self._db_session.execute(
            select(self._table.Ref_Id)
            .join_from(self._table, User)
            .where(self._table.Id == User.RetirementStatusId, User.Id == user_id)
        )

        return_items = []
        for item in result.fetchall():
            return_items.append(item[0])
        if not return_items:
            raise DoesNotExist(f"Retirement status does not exist")
        return return_items
