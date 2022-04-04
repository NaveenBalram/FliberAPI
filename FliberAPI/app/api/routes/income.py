import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.income import OutIncomeSchema, InIncomeSchema, IncomeSchema
from app.service.income import IncomeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_income(
    payload: InIncomeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save income data."""
    income_service = IncomeService(db)
    income = await income_service.create(payload)
    return income


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_income(payload: IncomeSchema, db: AsyncSession = Depends(get_db)):
    """ api to update income data."""
    income_service = IncomeService(db)
    await income_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=OutIncomeSchema)
async def get_income(uuid: UUID, db: AsyncSession = Depends(get_db)) -> OutIncomeSchema:
    """ api to fetch income data by id."""
    income_service = IncomeService(db)
    income = await income_service.get_by_id(uuid)
    return income


@router.get("/", status_code=status.HTTP_200_OK)
async def get_income(db: AsyncSession = Depends(get_db)):
    """ api to fetch all income data. """
    income_service = IncomeService(db)
    income = await income_service.get_all()
    return income


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_income(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete income data by id."""
    income_service = IncomeService(db)
    await income_service.delete(uuid)


# @router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
# async def delete_income_by_user_id(user_id: UUID, db: AsyncSession = Depends(get_db)):
#     """ api to save income data."""
#     income_service = IncomeService(db)
#     await income_service.delete(user_id)
