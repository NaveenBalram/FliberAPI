import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.bank_branches import BankBranchesRepository
from app.models.schema.bank_branches import (
    InBankBranchesSchema,
    BankBranchesSchema,
)

logger = logging.getLogger(__name__)


class BankBranchesService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._bank_branches_repository = BankBranchesRepository(self._db_session)

    async def create(self, payload: InBankBranchesSchema):
        bank_branches = await self._bank_branches_repository.create(payload)

        return bank_branches

    async def get_by_id(self, uuid: UUID):
        bank_branches = await self._bank_branches_repository.get_by_id(uuid)
        return bank_branches

    async def get_all(self):
        bank_branches = await self._bank_branches_repository.get_all()
        return bank_branches

    async def delete(self, uuid: UUID):
        await self._bank_branches_repository.delete(uuid)

    async def update(self, payload: BankBranchesSchema):
        await self._bank_branches_repository.update(payload)

    async def delete_bank_branches_by_user_id(self, user_id: UUID):
        await self._bank_branches_repository.delete_by_user_id(user_id)
