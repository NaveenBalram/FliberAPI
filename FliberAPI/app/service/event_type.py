import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.event_type import EventTypeRepository
from app.models.schema.event_type import (
    InEventTypeSchema,
    EventTypeSchema,
)

logger = logging.getLogger(__name__)


class EventTypeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._event_type_repository = EventTypeRepository(self._db_session)

    async def create(self, payload: InEventTypeSchema):
        event_type = await self._event_type_repository.create(payload)

        return event_type

    async def get_by_id(self, uuid: UUID):
        event_type = await self._event_type_repository.get_by_id(uuid)
        return event_type

    async def get_all(self):
        event_type = await self._event_type_repository.get_all()
        return event_type

    async def delete(self, uuid: UUID):
        await self._event_type_repository.delete(uuid)

    async def update(self, payload: EventTypeSchema):
        await self._event_type_repository.update(payload)

    async def delete_event_type_by_user_id(self, user_id: UUID):
        await self._event_type_repository.delete_by_user_id(user_id)
