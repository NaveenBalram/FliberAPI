import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.morning_star_navs import (
    OutMorningStarNavsSchema,
    InMorningStarNavsSchema,
    MorningStarNavsSchemaBase,
    MorningStarNavsSchema,
)
from app.service.morning_star_navs import MorningStarNavsService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_morning_star_navs(
    payload: InMorningStarNavsSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save morning star navs data. """
    morning_star_navs_service = MorningStarNavsService(db)
    morning_star_navs = await morning_star_navs_service.create(payload)
    return morning_star_navs


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_morning_star_navs(
    payload: MorningStarNavsSchema, db: AsyncSession = Depends(get_db)
):
    """ api to  morning star navs data. """
    morning_star_navs_service = MorningStarNavsService(db)
    await morning_star_navs_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_morning_star_navs(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to get morning star navs data by id. """
    morning_star_navs_service = MorningStarNavsService(db)
    morning_star_navs = await morning_star_navs_service.get_by_id(uuid)
    return morning_star_navs


@router.get("/", status_code=status.HTTP_200_OK)
async def get_morning_star_navs(db: AsyncSession = Depends(get_db)):
    """ api to get morning star navs data. """
    morning_star_navs_service = MorningStarNavsService(db)
    morning_star_navs = await morning_star_navs_service.get_all()
    return morning_star_navs


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_morning_star_navs(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete morning star navs data by id. """
    morning_star_navs_service = MorningStarNavsService(db)
    await morning_star_navs_service.delete(uuid)
