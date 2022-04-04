import logging
from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.service.calculations import CalculationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/SustainabilityScore")
async def sustainability_score(
        user_id: UUID, module_type: int, db: AsyncSession = Depends(get_db)
):
    score = CalculationService(db)
    return await score.sustainability_score(user_id, module_type)


@router.get("/RRScoreCalculation", status_code=status.HTTP_201_CREATED)
async def rr_score_calculation(
        user_id: UUID,
        module_type: int,
        retirement_age: int,
        db: AsyncSession = Depends(get_db),
):
    score = CalculationService(db)
    return await score.get_rr_score_calculation(
        user_id, module_type, retirement_age
    )


@router.get("/RiskProfile", status_code=status.HTTP_200_OK)
async def get_rr_score(
        user_id: UUID, module_type: int, db: AsyncSession = Depends(get_db)
):
    calculation_service = CalculationService(db)
    return await calculation_service.get_risk_profile_calculation(
        user_id=user_id, module_type=module_type
    )


@router.get("/PostRetirementScore", status_code=status.HTTP_200_OK)
async def get_rr_score(
        user_id: UUID, constraint: bool, amount: Optional[float] = 0, db: AsyncSession = Depends(get_db)
):
    calculate_service = CalculationService(db)
    return await calculate_service.post_retirement(user_id, constraint, amount)


@router.get('/futureValue')
def feature_value(intial_investment: float, interest_rate: float, investment_period: int, growth_rate: float):
    cal = ((1 + interest_rate / 100) ** investment_period - (1 + growth_rate / 100) ** investment_period) / (
            (interest_rate / 100) - (growth_rate / 100))
    fv = intial_investment * cal * (1 + interest_rate / 100)
    return {"futureValue": round(fv, 2)}


@router.get('/IncreasingSIPAmount')
def inccresing_sip_amount(future_value: float, interest_rate: float, investment_period: int, growth_rate: float):
    cal = (interest_rate / 100 - growth_rate / 100) / ((1 + interest_rate / 100) * (
            (1 + interest_rate / 100) ** investment_period - (1 + growth_rate / 100) ** investment_period))
    sip_amount = future_value * cal
    return {"IncreasingSIPAmount": round(sip_amount, 2)}
    fv = intial_investment * cal
    return {"futureValue": round(fv, 2)}
