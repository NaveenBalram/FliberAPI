import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.expense_type import (
    OutExpenseTypeSchema,
    InExpenseTypeSchema,
    ExpenseTypeSchemaBase,
    ExpenseTypeSchema,
)
from app.service.expense_type import ExpenseTypeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_expense_type(
    payload: InExpenseTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save expense type data. """
    expense_type_service = ExpenseTypeService(db)
    expense_type = await expense_type_service.create(payload)
    return expense_type


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_expense_type(
    payload: ExpenseTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update expense type data. """
    expense_type_service = ExpenseTypeService(db)
    await expense_type_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK
)
async def get_expense_type(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch expense type data by id. """
    expense_type_service = ExpenseTypeService(db)
    expense_type = await expense_type_service.get_by_id(uuid)
    return expense_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_expense_type(db: AsyncSession = Depends(get_db)):
    """ api to fetch all expense type data. """
    expense_type_service = ExpenseTypeService(db)
    expense_type = await expense_type_service.get_all()
    return expense_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_expense_type(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete expense type data by id. """
    expense_type_service = ExpenseTypeService(db)
    return await expense_type_service.delete(uuid)


# @router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
# async def delete_expense_type_by_user_id(
#     user_id: UUID, db: AsyncSession = Depends(get_db)
# ):
#     expense_type_service = ExpenseTypeService(db)
#     return await expense_type_service.delete(user_id)
