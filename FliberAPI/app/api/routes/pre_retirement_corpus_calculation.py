import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.pre_retirement_corpus_calculation import (
    InPreRetirementCorpusCalculationSchema,
    PreRetirementCorpusCalculationSchema,
)
from app.service.pre_retirement_corpus_calculation import (
    PreRetirementCorpusCalculationService,
)

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_pre_retirement_corpus_calculation(
        payload: InPreRetirementCorpusCalculationSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save pre retirement corpus calculation data. """
    pre_retirement_corpus_calculation_service = PreRetirementCorpusCalculationService(
        db
    )
    pre_retirement_corpus_calculation = (
        await pre_retirement_corpus_calculation_service.corpus_calculation(payload)
    )
    return pre_retirement_corpus_calculation


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_pre_retirement_corpus_calculation(
        payload: PreRetirementCorpusCalculationSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update pre retirement corpus calculation data. """
    pre_retirement_corpus_calculation_service = PreRetirementCorpusCalculationService(
        db
    )
    await pre_retirement_corpus_calculation_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_pre_retirement_corpus_calculation(
        uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to get pre retirement corpus calculation data by id. """
    pre_retirement_corpus_calculation_service = PreRetirementCorpusCalculationService(
        db
    )
    pre_retirement_corpus_calculation = (
        await pre_retirement_corpus_calculation_service.get_by_id(uuid)
    )
    return pre_retirement_corpus_calculation


@router.get("/", status_code=status.HTTP_200_OK)
async def get_pre_retirement_corpus_calculation(db: AsyncSession = Depends(get_db)):
    """ api to get pre retirement corpus calculation data. """
    pre_retirement_corpus_calculation_service = PreRetirementCorpusCalculationService(
        db
    )
    pre_retirement_corpus_calculation = (
        await pre_retirement_corpus_calculation_service.get_all()
    )
    return pre_retirement_corpus_calculation


@router.delete("/{uuid]", status_code=status.HTTP_200_OK)
async def delete_pre_retirement_corpus_calculation(
        uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete pre retirement corpus calculation data by id. """
    pre_retirement_corpus_calculation_service = PreRetirementCorpusCalculationService(
        db
    )
    await pre_retirement_corpus_calculation_service.delete(uuid)
