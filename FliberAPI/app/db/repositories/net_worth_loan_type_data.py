from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_loan_type_data import NetWorthLoanTypeData
from app.models.schema.net_worth_loan_type_data import NetWorthLoanTypeDataSchemaBase, NetWorthLoanTypeDataSchema, \
    InNetWorthLoanTypeDataSchema


class NetWorthLoanTypeDataRepository(
    BaseRepository[NetWorthLoanTypeDataSchemaBase, NetWorthLoanTypeDataSchema, NetWorthLoanTypeData]):
    @property
    def _in_schema(self) -> Type[NetWorthLoanTypeDataSchemaBase]:
        return InNetWorthLoanTypeDataSchema

    @property
    def _schema(self) -> Type[NetWorthLoanTypeDataSchema]:
        return NetWorthLoanTypeDataSchema

    @property
    def _table(self) -> Type[NetWorthLoanTypeData]:
        return NetWorthLoanTypeData
