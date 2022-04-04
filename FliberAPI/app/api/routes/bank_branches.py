import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.bank_branches import (
    OutBankBranchesSchema,
    InBankBranchesSchema,
    BankBranchesSchema,
)
from app.service.bank_branches import BankBranchesService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED,
)
async def create_bank_branches(
        payload: InBankBranchesSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save bank account type data. """
    bank_branches_service = BankBranchesService(db)
    bank_branches = await bank_branches_service.create(payload)
    return bank_branches


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_bank_branches(
        payload: BankBranchesSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update bank account type data. """
    bank_branches_service = BankBranchesService(db)
    await bank_branches_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK
)
async def get_bank_branches(
        uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch bank account type data id. """
    bank_branches_service = BankBranchesService(db)
    bank_branches = await bank_branches_service.get_by_id(uuid)
    return bank_branches


@router.get("/", status_code=status.HTTP_200_OK)
async def get_bank_branches(db: AsyncSession = Depends(get_db)):
    """ api to fetch all bank account type data. """
    bank_branches_service = BankBranchesService(db)
    bank_branches = await bank_branches_service.get_all()
    return bank_branches


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_bank_branches(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete bank account type data by id. """
    bank_branches_service = BankBranchesService(db)
    return await bank_branches_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_bank_branches_by_user_id(
        user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to save bank account type data. """
    bank_branches_service = BankBranchesService(db)
    return await bank_branches_service.delete(user_id)
