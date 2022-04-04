from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.user_info import UserInfo
from app.models.schema.user_info import (
    UserInfoSchemaBase,
    UserInfoSchema,
    InUserInfoSchema,
)


class UserInfoRepository(BaseRepository[UserInfoSchemaBase, UserInfoSchema, UserInfo]):
    @property
    def _in_schema(self) -> Type[UserInfoSchemaBase]:
        return InUserInfoSchema

    @property
    def _schema(self) -> Type[UserInfoSchema]:
        return UserInfoSchema

    @property
    def _table(self) -> Type[UserInfo]:
        return UserInfo
