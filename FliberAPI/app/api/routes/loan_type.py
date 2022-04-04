import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.loan_type import (
    OutLoanTypeSchema,
    InLoanTypeSchema,
    LoanTypeSchema,
)
from app.service.loan_type import LoanTypeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OutLoanTypeSchema)
async def create_loan_type(
    payload: InLoanTypeSchema, db: AsyncSession = Depends(get_db)
) -> OutLoanTypeSchema:
    """ api to save loan type data. """
    loan_type_service = LoanTypeService(db)
    loan_type = await loan_type_service.create(payload)
    return loan_type


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_loan_type(payload: LoanTypeSchema, db: AsyncSession = Depends(get_db)):
    """ api to get loan type data. """
    loan_type_service = LoanTypeService(db)
    await loan_type_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=OutLoanTypeSchema)
async def get_loan_type(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutLoanTypeSchema:
    """ api to  loan type data. """
    loan_type_service = LoanTypeService(db)
    loan_type = await loan_type_service.get_by_id(uuid)
    return loan_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_loan_type(db: AsyncSession = Depends(get_db)):
    """ api to get loan type data. """
    loan_type_service = LoanTypeService(db)
    loan_type = await loan_type_service.get_all()
    return loan_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_loan_type(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete loan type data by id. """
    loan_type_service = LoanTypeService(db)
    await loan_type_service.delete(uuid)



