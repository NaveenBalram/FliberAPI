import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.expense_category import (
    OutExpenseCategorySchema,
    InExpenseCategorySchema,
    ExpenseCategorySchema,
)
from app.service.expense_category import ExpenseCategoryService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutExpenseCategorySchema
)
async def create_expense_category(
    payload: InExpenseCategorySchema, db: AsyncSession = Depends(get_db)
):
    """ api to save expense category data. """
    expense_category_service = ExpenseCategoryService(db)
    expense_category = await expense_category_service.create(payload)
    return expense_category


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_expense_category(
    payload: ExpenseCategorySchema, db: AsyncSession = Depends(get_db)
):
    """ api to update expense category data. """
    expense_category_service = ExpenseCategoryService(db)
    await expense_category_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK
)
async def get_expense_category(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch expense category data by id. """
    expense_category_service = ExpenseCategoryService(db)
    expense_category = await expense_category_service.get_by_id(uuid)
    return expense_category


@router.get("/", status_code=status.HTTP_200_OK)
async def get_expense_category(db: AsyncSession = Depends(get_db)):
    """ api to fetch all expense category data. """
    expense_category_service = ExpenseCategoryService(db)
    expense_category = await expense_category_service.get_all()
    return expense_category


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_expense_category(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete expense category by id. """
    expense_category_service = ExpenseCategoryService(db)
    return await expense_category_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_expense_category_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete expense category by user id. """
    expense_category_service = ExpenseCategoryService(db)
    return await expense_category_service.delete(user_id)
