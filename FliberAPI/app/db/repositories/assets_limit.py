from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.assets_limit import AssetsLimit
from app.models.schema.assets_limit import (
    AssetsLimitSchemaBase,
    AssetsLimitSchema,
    AssetsLimitSchema,
    InAssetsLimitSchema,
)


class AssetsLimitRepository(
    BaseRepository[AssetsLimitSchemaBase, AssetsLimitSchema, AssetsLimit]
):
    @property
    def _in_schema(self) -> Type[AssetsLimitSchemaBase]:
        return InAssetsLimitSchema

    @property
    def _schema(self) -> Type[AssetsLimitSchema]:
        return AssetsLimitSchema

    @property
    def _table(self) -> Type[AssetsLimit]:
        return AssetsLimit
