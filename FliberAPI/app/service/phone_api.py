import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.phone_api import PhoneApiRepository
from app.models.schema.phone_api import (
    PhoneApiSchema,
    InPhoneApiSchema,
)

logger = logging.getLogger(__name__)


class PhoneApiService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._phone_api_repository = PhoneApiRepository(self._db_session)

    async def create(self, payload: InPhoneApiSchema):

        if len(str(payload.Phone)) != 10:
            raise ValueError("Enter 10 digit phone number")

        if not payload.Phone.isdigit():
            raise ValueError("Enter 10 digit phone number")

        return await self._phone_api_repository.create(payload)

    async def get_by_id(self, uuid: UUID):
        return await self._phone_api_repository.get_by_id(uuid)

    async def get_all(self):
        phone_api = await self._phone_api_repository.get_all()
        return phone_api

    async def delete(self, uuid: UUID):
        await self._phone_api_repository.delete(uuid)

    async def update(self, payload: PhoneApiSchema):
        if len(str(payload.Phone)) != 10:
            raise ValueError("Enter 10 digit phone number")

        if not payload.Phone.isdigit():
            raise ValueError("Enter 10 digit phone number")

        await self._phone_api_repository.update(payload)
