import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.investment_profile import (
    OutInvestmentProfileSchema,
    InInvestmentProfileSchema,
    InvestmentProfileSchema,
)
from app.service.investment_profile import InvestmentProfileService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutInvestmentProfileSchema
)
async def create_investment_profile(
    payload: InInvestmentProfileSchema, db: AsyncSession = Depends(get_db)
) -> OutInvestmentProfileSchema:
    investment_profile_service = InvestmentProfileService(db)
    investment_profile = await investment_profile_service.create(payload)
    return investment_profile


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_investment_profile(
    payload: InvestmentProfileSchema, db: AsyncSession = Depends(get_db)
):
    investment_profile_service = InvestmentProfileService(db)
    await investment_profile_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutInvestmentProfileSchema
)
async def get_investment_profile(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutInvestmentProfileSchema:
    investment_profile_service = InvestmentProfileService(db)
    investment_profile = await investment_profile_service.get_by_id(uuid)
    return investment_profile


@router.get("/", status_code=status.HTTP_200_OK)
async def get_investment_profile(db: AsyncSession = Depends(get_db)):
    investment_profile_service = InvestmentProfileService(db)
    investment_profile = await investment_profile_service.get_all()
    return investment_profile


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_investment_profile(uuid: UUID, db: AsyncSession = Depends(get_db)):
    investment_profile_service = InvestmentProfileService(db)
    await investment_profile_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_investment_profile_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    investment_profile_service = InvestmentProfileService(db)
    await investment_profile_service.delete(user_id)
