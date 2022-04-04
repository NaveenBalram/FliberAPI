import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.event_type import (
    OutEventTypeSchema,
    InEventTypeSchema,
    EventTypeSchema,
)
from app.service.event_type import EventTypeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutEventTypeSchema
)
async def create_event_type(
    payload: InEventTypeSchema, db: AsyncSession = Depends(get_db)
):
    """api to save event type data."""
    event_type_service = EventTypeService(db)
    event_type = await event_type_service.create(payload)
    return event_type


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_event_type(
    payload: EventTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save event type data"""
    event_type_service = EventTypeService(db)
    await event_type_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutEventTypeSchema
)
async def get_event_type(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to update event type data"""
    event_type_service = EventTypeService(db)
    event_type = await event_type_service.get_by_id(uuid)
    return event_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_event_type(db: AsyncSession = Depends(get_db)):
    """ api to fetch event type data"""
    event_type_service = EventTypeService(db)
    event_type = await event_type_service.get_all()
    return event_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_event_type(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete event type data by id"""
    event_type_service = EventTypeService(db)
    return await event_type_service.delete(uuid)

