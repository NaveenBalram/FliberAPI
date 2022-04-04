import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from app.service.asset_advisory import AssetAdvisoryService
from app.api.dependencies.db import get_db

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/")
async def asset_advisory(
        risk_category : str,
        funding : float,
        timetoretierment : int,
        db: AsyncSession = Depends(get_db)
):
    asset_advisory = AssetAdvisoryService(db)
    asset_advisory = asset_advisory.get_advisory(risk_category,funding,timetoretierment)
    return await asset_advisory

