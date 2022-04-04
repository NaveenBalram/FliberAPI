import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.epfo_auto_fetch import OutEpfoAutoFetchSchema, InEpfoAutoFetchSchema, EpfoAutoFetchSchemaBase, EpfoAutoFetchSchema
from app.service.epfo_auto_fetch import EpfoAutoFetchService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_epfo_auto_fetch(payload: InEpfoAutoFetchSchema, db: AsyncSession = Depends(get_db)):
    epfo_auto_fetch_service = EpfoAutoFetchService(db)
    epfo_auto_fetch = await epfo_auto_fetch_service.create(payload)
    return epfo_auto_fetch


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_epfo_auto_fetch(payload: EpfoAutoFetchSchema, db: AsyncSession = Depends(get_db)):
    epfo_auto_fetch_service = EpfoAutoFetchService(db)
    await epfo_auto_fetch_service.update(payload)


@router.get("/'uuid'", status_code=status.HTTP_200_OK)
async def get_epfo_auto_fetch(uuid: UUID, db: AsyncSession = Depends(get_db)):
    epfo_auto_fetch_service = EpfoAutoFetchService(db)
    epfo_auto_fetch = await epfo_auto_fetch_service.get_by_id(uuid)
    return epfo_auto_fetch


@router.get("/", status_code=status.HTTP_200_OK)
async def get_epfo_auto_fetch(db: AsyncSession = Depends(get_db)):
    epfo_auto_fetch_service = EpfoAutoFetchService(db)
    epfo_auto_fetch = await epfo_auto_fetch_service.get_all()
    return epfo_auto_fetch


@router.delete("/'uuid'", status_code=status.HTTP_200_OK)
async def delete_epfo_auto_fetch(uuid: UUID, db: AsyncSession = Depends(get_db)):
    epfo_auto_fetch_service = EpfoAutoFetchService(db)
    await epfo_auto_fetch_service.delete(uuid)

    