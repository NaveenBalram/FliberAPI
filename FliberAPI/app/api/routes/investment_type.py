import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.investment_type import (
    OutInvestmentTypeSchema,
    InInvestmentTypeSchema,
    InvestmentTypeSchema,
)
from app.service.investment_type import InvestmentTypeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutInvestmentTypeSchema
)
async def create_investment_type(
    payload: InInvestmentTypeSchema, db: AsyncSession = Depends(get_db)
) -> OutInvestmentTypeSchema:
    investment_type_service = InvestmentTypeService(db)
    investment_type = await investment_type_service.create(payload)
    return investment_type


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_investment_type(
    payload: InvestmentTypeSchema, db: AsyncSession = Depends(get_db)
):
    investment_type_service = InvestmentTypeService(db)
    await investment_type_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutInvestmentTypeSchema
)
async def get_investment_type(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutInvestmentTypeSchema:
    investment_type_service = InvestmentTypeService(db)
    investment_type = await investment_type_service.get_by_id(uuid)
    return investment_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_investment_type(db: AsyncSession = Depends(get_db)):
    investment_type_service = InvestmentTypeService(db)
    investment_type = await investment_type_service.get_all()
    return investment_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_investment_type(uuid: UUID, db: AsyncSession = Depends(get_db)):
    investment_type_service = InvestmentTypeService(db)
    await investment_type_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_investment_type_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    investment_type_service = InvestmentTypeService(db)
    await investment_type_service.delete(user_id)
