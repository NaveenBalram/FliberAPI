import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.net_worth_loan_type_data import NetWorthLoanTypeDataRepository
from app.models.schema.net_worth_loan_type_data import NetWorthLoanTypeDataSchema, InNetWorthLoanTypeDataSchema

logger = logging.getLogger(__name__)


class NetWorthLoanTypeDataService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session

        self._net_worth_loan_type_data_repository = NetWorthLoanTypeDataRepository(self._db_session)

    async def create(self, payload: InNetWorthLoanTypeDataSchema):
        net_worth_loan_type_data = await self._net_worth_loan_type_data_repository.create(payload)

        return net_worth_loan_type_data

    async def get_by_id(self, uuid: UUID):
        net_worth_loan_type_data = await self._net_worth_loan_type_data_repository.get_by_id(uuid)
        return net_worth_loan_type_data

    async def get_all(self):
        net_worth_loan_type_data = await self._net_worth_loan_type_data_repository.get_all()
        return net_worth_loan_type_data

    async def delete(self, uuid: UUID):
        await self._net_worth_loan_type_data_repository.delete(uuid)

    async def update(self, payload: NetWorthLoanTypeDataSchema):
        await self._net_worth_loan_type_data_repository.update(payload)
