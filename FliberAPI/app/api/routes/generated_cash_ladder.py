import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.generated_cash_ladder import (
    OutGeneratedCashLadderSchema,
    InGeneratedCashLadderSchema,
    GeneratedCashLadderSchema,
)
from app.service.generated_cash_ladder import GeneratedCashLadderService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
async def create_generated_cash_ladder(
    payload: InGeneratedCashLadderSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save generated cash ladder. """
    generated_cash_ladder_service = GeneratedCashLadderService(db)
    generated_cash_ladder = await generated_cash_ladder_service.create(payload)
    return generated_cash_ladder


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_generated_cash_ladder(
    payload: GeneratedCashLadderSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update generated cash ladder. """
    generated_cash_ladder_service = GeneratedCashLadderService(db)
    await generated_cash_ladder_service.update(payload)


@router.get(
    "/{uuid}",
    status_code=status.HTTP_200_OK
)
async def get_generated_cash_ladder(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch generated cash ladder by id. """
    generated_cash_ladder_service = GeneratedCashLadderService(db)
    generated_cash_ladder = await generated_cash_ladder_service.get_by_id(uuid)
    return generated_cash_ladder


@router.get("/", status_code=status.HTTP_200_OK)
async def get_generated_cash_ladder(db: AsyncSession = Depends(get_db)):
    """ api to fetch all generated cash ladder. """
    generated_cash_ladder_service = GeneratedCashLadderService(db)
    generated_cash_ladder = await generated_cash_ladder_service.get_all()
    return generated_cash_ladder


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_generated_cash_ladder(uuid: UUID, db: AsyncSession = Depends(get_db)):
    generated_cash_ladder_service = GeneratedCashLadderService(db)
    await generated_cash_ladder_service.delete(uuid)


# @router.get("/generate/{uuid}", status_code=status.HTTP_200_OK)
# async def generate_cash_ladder(uuid: UUID, db: AsyncSession = Depends(get_db)):
#     generated_cash_ladder_service = GeneratedCashLadderService(db)
#     await generated_cash_ladder_service.generate(uuid)

@router.get("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_generated_cash_ladder_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    generated_cash_ladder_service = GeneratedCashLadderService(db)
    await generated_cash_ladder_service.get_by_user_id(user_id)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_generated_cash_ladder_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    generated_cash_ladder_service = GeneratedCashLadderService(db)
    await generated_cash_ladder_service.delete(user_id)
