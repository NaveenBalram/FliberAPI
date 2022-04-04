import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.net_worth_loan_type_data import InNetWorthLoanTypeDataSchema, NetWorthLoanTypeDataSchema
from app.service.net_worth_loan_type_data import NetWorthLoanTypeDataService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_net_worth_loan_type_data(payload: InNetWorthLoanTypeDataSchema, db: AsyncSession = Depends(get_db)):
    net_worth_loan_type_data_service = NetWorthLoanTypeDataService(db)
    net_worth_loan_type_data = await net_worth_loan_type_data_service.create(payload)
    return net_worth_loan_type_data


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_net_worth_loan_type_data(payload: NetWorthLoanTypeDataSchema, db: AsyncSession = Depends(get_db)):
    net_worth_loan_type_data_service = NetWorthLoanTypeDataService(db)
    await net_worth_loan_type_data_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_net_worth_loan_type_data(uuid: UUID, db: AsyncSession = Depends(get_db)):
    net_worth_loan_type_data_service = NetWorthLoanTypeDataService(db)
    net_worth_loan_type_data = await net_worth_loan_type_data_service.get_by_id(uuid)
    return net_worth_loan_type_data


@router.get("/", status_code=status.HTTP_200_OK)
async def get_net_worth_loan_type_data(db: AsyncSession = Depends(get_db)):
    net_worth_loan_type_data_service = NetWorthLoanTypeDataService(db)
    net_worth_loan_type_data = await net_worth_loan_type_data_service.get_all()
    return net_worth_loan_type_data


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_net_worth_loan_type_data(uuid: UUID, db: AsyncSession = Depends(get_db)):
    net_worth_loan_type_data_service = NetWorthLoanTypeDataService(db)
    await net_worth_loan_type_data_service.delete(uuid)
