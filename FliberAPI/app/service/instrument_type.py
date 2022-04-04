import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.instrument_type import InstrumentTypeRepository
from app.models.schema.instrument_type import (
    InInstrumentTypeSchema,
    InstrumentTypeSchema,
)

logger = logging.getLogger(__name__)


class InstrumentTypeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._instrument_type_repository = InstrumentTypeRepository(self._db_session)

    async def create(self, payload: InInstrumentTypeSchema):
        instrument_type = await self._instrument_type_repository.create(payload)

        return instrument_type

    async def get_by_id(self, uuid: UUID):
        instrument_type = await self._instrument_type_repository.get_by_id(uuid)
        return instrument_type

    async def get_all(self):
        instrument_type = await self._instrument_type_repository.get_all()
        return instrument_type

    async def delete(self, uuid: UUID):
        await self._instrument_type_repository.delete(uuid)

    async def update(self, payload: InstrumentTypeSchema):
        await self._instrument_type_repository.update(payload)

    async def delete_instrument_type_by_user_id(self, user_id: UUID):
        await self._instrument_type_repository.delete_by_user_id(user_id)
