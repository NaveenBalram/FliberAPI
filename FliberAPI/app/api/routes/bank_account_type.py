import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.bank_account_type import (
    OutBankAccountTypeSchema,
    InBankAccountTypeSchema,
    BankAccountTypeSchema,
)
from app.service.bank_account_type import BankAccountTypeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED,
)
async def create_bank_account_type(
    payload: InBankAccountTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save bank account type data. """
    bank_account_type_service = BankAccountTypeService(db)
    bank_account_type = await bank_account_type_service.create(payload)
    return bank_account_type


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_bank_account_type(
    payload: BankAccountTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update bank account type data. """
    bank_account_type_service = BankAccountTypeService(db)
    await bank_account_type_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK,
)
async def get_bank_account_type(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch bank account type data by id. """
    bank_account_type_service = BankAccountTypeService(db)
    bank_account_type = await bank_account_type_service.get_by_id(uuid)
    return bank_account_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_bank_account_type(db: AsyncSession = Depends(get_db)):
    """ api to fetch all bank account type data. """
    bank_account_type_service = BankAccountTypeService(db)
    bank_account_type = await bank_account_type_service.get_all()
    return bank_account_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_bank_account_type(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete bank account type data by id. """
    bank_account_type_service = BankAccountTypeService(db)
    return await bank_account_type_service.delete(uuid)

