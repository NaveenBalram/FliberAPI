import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.source_of_wealth import (
    OutSourceOfWealthSchema,
    InSourceOfWealthSchema,
    SourceOfWealthSchema,
)
from app.service.source_of_wealth import SourceOfWealthService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutSourceOfWealthSchema
)
async def create_source_of_wealth(
    payload: InSourceOfWealthSchema, db: AsyncSession = Depends(get_db)
) -> OutSourceOfWealthSchema:
    """ api to save source of wealth data. """
    source_of_wealth_service = SourceOfWealthService(db)
    source_of_wealth = await source_of_wealth_service.create(payload)
    return source_of_wealth


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_source_of_wealth(
    payload: SourceOfWealthSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update source of wealth data. """
    source_of_wealth_service = SourceOfWealthService(db)
    await source_of_wealth_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutSourceOfWealthSchema
)
async def get_source_of_wealth(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutSourceOfWealthSchema:
    """ api to get source of wealth data by id. """
    source_of_wealth_service = SourceOfWealthService(db)
    source_of_wealth = await source_of_wealth_service.get_by_id(uuid)
    return source_of_wealth


@router.get("/", status_code=status.HTTP_200_OK)
async def get_source_of_wealth(db: AsyncSession = Depends(get_db)):
    """ api to get source of wealth data. """
    source_of_wealth_service = SourceOfWealthService(db)
    source_of_wealth = await source_of_wealth_service.get_all()
    return source_of_wealth


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_source_of_wealth(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete source of wealth data by id. """
    source_of_wealth_service = SourceOfWealthService(db)
    await source_of_wealth_service.delete(uuid)

