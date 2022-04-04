import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.sustainability_score import SustainabilityScoreSchema
from app.service.sustainability_score import SustainabilityScoreService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/SustainabilityScore")
async def sustainability_score(
        user_id: UUID, module_type: int, db: AsyncSession = Depends(get_db)
):
    """ api to save sustainability score data. """
    score = SustainabilityScoreService(db)
    return await score.sustainability_score(user_id, module_type)


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_sustainability_score(payload: SustainabilityScoreSchema, db: AsyncSession = Depends(get_db)):
    """ api to update sustainability score data. """
    sustainability_score_service = SustainabilityScoreService(db)
    await sustainability_score_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_sustainability_score(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to get sustainability score data by id. """
    sustainability_score_service = SustainabilityScoreService(db)
    sustainability_score = await sustainability_score_service.get_by_id(uuid)
    return sustainability_score


@router.get("/", status_code=status.HTTP_200_OK)
async def get_sustainability_score(db: AsyncSession = Depends(get_db)):
    """ api to get sustainability score data. """
    sustainability_score_service = SustainabilityScoreService(db)
    sustainability_score = await sustainability_score_service.get_all()
    return sustainability_score


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_sustainability_score(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete sustainability score data by id. """
    sustainability_score_service = SustainabilityScoreService(db)
    await sustainability_score_service.delete(uuid)
