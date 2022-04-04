import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.marital_status import OutMaritalStatusSchema, InMaritalStatusSchema, MaritalStatusSchemaBase, MaritalStatusSchema
from app.service.marital_status import MaritalStatusService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_marital_status(payload: InMaritalStatusSchema, db: AsyncSession = Depends(get_db)):
    marital_status_service = MaritalStatusService(db)
    marital_status = await marital_status_service.create(payload)
    return marital_status


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_marital_status(payload: MaritalStatusSchema, db: AsyncSession = Depends(get_db)):
    marital_status_service = MaritalStatusService(db)
    await marital_status_service.update(payload)


@router.get("/'uuid'", status_code=status.HTTP_200_OK)
async def get_marital_status(uuid: UUID, db: AsyncSession = Depends(get_db)):
    marital_status_service = MaritalStatusService(db)
    marital_status = await marital_status_service.get_by_id(uuid)
    return marital_status


@router.get("/", status_code=status.HTTP_200_OK)
async def get_marital_status(db: AsyncSession = Depends(get_db)):
    marital_status_service = MaritalStatusService(db)
    marital_status = await marital_status_service.get_all()
    return marital_status


@router.delete("/'uuid'", status_code=status.HTTP_200_OK)
async def delete_marital_status(uuid: UUID, db: AsyncSession = Depends(get_db)):
    marital_status_service = MaritalStatusService(db)
    await marital_status_service.delete(uuid)

    