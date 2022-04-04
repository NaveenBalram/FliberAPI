import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.users_re_balance_sheet import (
    OutUsersReBalanceSheetSchema,
    InUsersReBalanceSheetSchema,
    UsersReBalanceSheetSchemaBase,
    UsersReBalanceSheetSchema,
)
from app.service.users_re_balance_sheet import UsersReBalanceSheetService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_users_re_balance_sheet(
    payload: InUsersReBalanceSheetSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save users re balance sheet data. """
    users_re_balance_sheet_service = UsersReBalanceSheetService(db)
    users_re_balance_sheet = await users_re_balance_sheet_service.create(payload)
    return users_re_balance_sheet


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_users_re_balance_sheet(
    payload: UsersReBalanceSheetSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update users re balance sheet data. """
    users_re_balance_sheet_service = UsersReBalanceSheetService(db)
    await users_re_balance_sheet_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_users_re_balance_sheet(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to get users re balance sheet data by id. """
    users_re_balance_sheet_service = UsersReBalanceSheetService(db)
    users_re_balance_sheet = await users_re_balance_sheet_service.get_by_id(uuid)
    return users_re_balance_sheet


@router.get("/", status_code=status.HTTP_200_OK)
async def get_users_re_balance_sheet(db: AsyncSession = Depends(get_db)):
    """ api to get users re balance sheet data. """
    users_re_balance_sheet_service = UsersReBalanceSheetService(db)
    users_re_balance_sheet = await users_re_balance_sheet_service.get_all()
    return users_re_balance_sheet


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_users_re_balance_sheet(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete users re balance sheet data by id. """
    users_re_balance_sheet_service = UsersReBalanceSheetService(db)
    await users_re_balance_sheet_service.delete(uuid)
