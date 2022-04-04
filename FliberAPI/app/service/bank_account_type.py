import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.bank_account_type import BankAccountTypeRepository
from app.models.schema.bank_account_type import (
    InBankAccountTypeSchema,
    BankAccountTypeSchema,
)

logger = logging.getLogger(__name__)


class BankAccountTypeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._bank_account_type_repository = BankAccountTypeRepository(self._db_session)

    async def create(
            self, payload: InBankAccountTypeSchema
    ):
        bank_account_type = await self._bank_account_type_repository.create(payload)

        return bank_account_type

    async def get_by_id(self, uuid: UUID):
        bank_account_type = await self._bank_account_type_repository.get_by_id(uuid)
        return bank_account_type

    async def get_all(self):
        bank_account_type = await self._bank_account_type_repository.get_all()
        return bank_account_type

    async def delete(self, uuid: UUID):
        await self._bank_account_type_repository.delete(uuid)

    async def update(self, payload: BankAccountTypeSchema):
        await self._bank_account_type_repository.update(payload)

    async def delete_bank_account_type_by_user_id(self, user_id: UUID):
        await self._bank_account_type_repository.delete_by_user_id(user_id)
