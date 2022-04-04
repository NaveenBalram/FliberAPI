from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.signzy_account import SignzyAccount
from app.models.schema.signzy_account import (
    SignzyAccountSchemaBase,
    SignzyAccountSchema,
    InSignzyAccountSchema,
)


class SignzyAccountRepository(
    BaseRepository[SignzyAccountSchemaBase, SignzyAccountSchema, SignzyAccount]
):
    @property
    def _in_schema(self) -> Type[SignzyAccountSchemaBase]:
        return InSignzyAccountSchema

    @property
    def _schema(self) -> Type[SignzyAccountSchema]:
        return SignzyAccountSchema

    @property
    def _table(self) -> Type[SignzyAccount]:
        return SignzyAccount
