import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.loan_type import LoanTypeRepository
from app.models.schema.loan_type import (
    InLoanTypeSchema,
    LoanTypeSchema,
)

logger = logging.getLogger(__name__)


class LoanTypeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._loan_type_repository = LoanTypeRepository(self._db_session)

    async def create(self, payload: InLoanTypeSchema):
        loan_type = await self._loan_type_repository.create(payload)

        return loan_type

    async def get_by_id(self, uuid: UUID):
        loan_type = await self._loan_type_repository.get_by_id(uuid)
        return loan_type

    async def get_all(self):
        loan_type = await self._loan_type_repository.get_all()
        return loan_type

    async def delete(self, uuid: UUID):
        await self._loan_type_repository.delete(uuid)

    async def update(self, payload: LoanTypeSchema):
        await self._loan_type_repository.update(payload)

    async def delete_loan_type_by_user_id(self, user_id: UUID):
        await self._loan_type_repository.delete_by_user_id(user_id)
