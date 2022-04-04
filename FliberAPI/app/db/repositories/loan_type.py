from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.loan_type import LoanType
from app.models.schema.loan_type import (
    LoanTypeSchemaBase,
    LoanTypeSchema,
    InLoanTypeSchema,
)


class LoanTypeRepository(BaseRepository[LoanTypeSchemaBase, LoanTypeSchema, LoanType]):
    @property
    def _in_schema(self) -> Type[LoanTypeSchemaBase]:
        return InLoanTypeSchema

    @property
    def _schema(self) -> Type[LoanTypeSchema]:
        return LoanTypeSchema

    @property
    def _table(self) -> Type[LoanType]:
        return LoanType
