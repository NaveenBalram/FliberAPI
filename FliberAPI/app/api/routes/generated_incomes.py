import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.generated_incomes import (
    OutGeneratedIncomesSchema,
    InGeneratedIncomesSchema,
    GeneratedIncomesSchema,
)
from app.service.generated_incomes import GeneratedIncomesService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_generated_incomes(
    payload: InGeneratedIncomesSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save generated income data."""
    generated_incomes_service = GeneratedIncomesService(db)
    generated_incomes = await generated_incomes_service.create(payload)
    return generated_incomes


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_generated_incomes(
    payload: GeneratedIncomesSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save generated goals data."""
    generated_incomes_service = GeneratedIncomesService(db)
    await generated_incomes_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK,
)
async def get_generated_incomes(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch generated goals data by id."""
    generated_incomes_service = GeneratedIncomesService(db)
    generated_incomes = await generated_incomes_service.get_by_id(uuid)
    return generated_incomes


@router.get("/", status_code=status.HTTP_200_OK)
async def get_generated_incomes(db: AsyncSession = Depends(get_db)):
    """ api to fetch all generated goals data."""
    generated_incomes_service = GeneratedIncomesService(db)
    generated_incomes = await generated_incomes_service.get_all()
    return generated_incomes


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_generated_incomes(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete generated goals data by id."""
    generated_incomes_service = GeneratedIncomesService(db)
    await generated_incomes_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_generated_incomes_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete generated goals data by user id."""
    generated_incomes_service = GeneratedIncomesService(db)
    await generated_incomes_service.delete(user_id)
