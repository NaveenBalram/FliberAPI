import datetime
import uuid
from typing import Type

from sqlalchemy import update, select, insert

from app.db.repositories.base import BaseRepository
from app.db.tables.user_result import UserResult
from app.models.schema.user_result import (
    UserResultSchemaBase,
    UserResultSchema,
    InUserResultSchema,
)


class UserResultRepository(
    BaseRepository[UserResultSchemaBase, UserResultSchema, UserResult]
):
    @property
    def _in_schema(self) -> Type[UserResultSchemaBase]:
        return InUserResultSchema

    @property
    def _schema(self) -> Type[UserResultSchema]:
        return UserResultSchema

    @property
    def _table(self) -> Type[UserResult]:
        return UserResult

    async def update_result(self, risk_profile, user_id):
        stmt = select(self._table).where(self._table.UserId == user_id)

        result = await self._db_session.execute(stmt)
        return_items = []
        for item in result.fetchall():
            return_items.append(item)

        if return_items:
            stmt = (
                update(self._table)
                .values(RiskProfile=risk_profile)
                .where(self._table.UserId == user_id)
            )
        else:
            stmt = insert(self._table).values(
                Id=uuid.uuid4(),
                UserId=user_id,
                RiskProfile=risk_profile,
                CreatedOn=datetime.datetime.now(),
                UpdatedOn=datetime.datetime.now(),
                IsDeleted=False,
            )

        await self._db_session.execute(stmt)

        # return_items = []
        # for item in result.fetchall():
        #     return_items.append(item)
        # if not return_items:
        #     raise DoesNotExist(f"Risk Profile does not exist for this user.")
        # return return_items
