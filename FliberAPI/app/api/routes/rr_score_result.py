import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.rr_score_result import InRrScoreResultSchema, RrScoreResultSchema
from app.service.rr_score_result import RrScoreResultService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_rr_score_result(payload: InRrScoreResultSchema, db: AsyncSession = Depends(get_db)):
    rr_score_result_service = RrScoreResultService(db)
    rr_score_result = await rr_score_result_service.create(payload)
    return rr_score_result


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_rr_score_result(payload: RrScoreResultSchema, db: AsyncSession = Depends(get_db)):
    rr_score_result_service = RrScoreResultService(db)
    await rr_score_result_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_rr_score_result(uuid: UUID, db: AsyncSession = Depends(get_db)):
    rr_score_result_service = RrScoreResultService(db)
    rr_score_result = await rr_score_result_service.get_by_id(uuid)
    return rr_score_result


@router.get("/", status_code=status.HTTP_200_OK)
async def get_rr_score_result(db: AsyncSession = Depends(get_db)):
    rr_score_result_service = RrScoreResultService(db)
    rr_score_result = await rr_score_result_service.get_all()
    return rr_score_result


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_rr_score_result(uuid: UUID, db: AsyncSession = Depends(get_db)):
    rr_score_result_service = RrScoreResultService(db)
    await rr_score_result_service.delete(uuid)


@router.get("/by/{user_id}", status_code=status.HTTP_200_OK)
async def get_rr_score_result(user_id: UUID, db: AsyncSession = Depends(get_db)):
    rr_score_result_service = RrScoreResultService(db)
    rr_score_result = await rr_score_result_service.get_by_user_id(user_id)
    return rr_score_result
