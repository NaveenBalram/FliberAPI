import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.banks import OutBanksSchema, InBanksSchema, BanksSchema
from app.service.banks import BanksService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_banks(
    payload: InBanksSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save bank data. """
    banks_service = BanksService(db)
    banks = await banks_service.create(payload)
    return banks


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_banks(payload: BanksSchema, db: AsyncSession = Depends(get_db)):
    """ api to update bank data. """
    banks_service = BanksService(db)
    await banks_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=OutBanksSchema)
async def get_banks(uuid: UUID, db: AsyncSession = Depends(get_db)) -> OutBanksSchema:
    """ api to fetch bank data by id. """
    banks_service = BanksService(db)
    banks = await banks_service.get_by_id(uuid)
    return banks


@router.get("/", status_code=status.HTTP_200_OK)
async def get_banks(db: AsyncSession = Depends(get_db)):
    """ api to fetch all bank data. """
    banks_service = BanksService(db)
    banks = await banks_service.get_all()
    return banks


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_banks(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete bank data by id. """
    banks_service = BanksService(db)
    return await banks_service.delete(uuid)

