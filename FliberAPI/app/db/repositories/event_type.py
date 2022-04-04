from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.event_type import EventType
from app.models.schema.event_type import (
    EventTypeSchemaBase,
    EventTypeSchema,
    InEventTypeSchema,
)


class EventTypeRepository(
    BaseRepository[EventTypeSchemaBase, EventTypeSchema, EventType]
):
    @property
    def _in_schema(self) -> Type[EventTypeSchemaBase]:
        return InEventTypeSchema

    @property
    def _schema(self) -> Type[EventTypeSchema]:
        return EventTypeSchema

    @property
    def _table(self) -> Type[EventType]:
        return EventType
