from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.role import Role
from app.models.schema.role import RoleSchemaBase, RoleSchema, InRoleSchema


class RoleRepository(BaseRepository[RoleSchemaBase, RoleSchema, Role]):
    @property
    def _in_schema(self) -> Type[RoleSchemaBase]:
        return InRoleSchema

    @property
    def _schema(self) -> Type[RoleSchema]:
        return RoleSchema

    @property
    def _table(self) -> Type[Role]:
        return Role
