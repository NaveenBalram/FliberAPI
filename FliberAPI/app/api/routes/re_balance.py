import logging

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.re_balance import (
    ReBalanceSchemaBase,
    SIPReBalance,
)
from app.service.re_balance import ReBalanceService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_re_balance(
        payload: ReBalanceSchemaBase, db: AsyncSession = Depends(get_db)
):
    """ api to save re balance data. """
    re_balance_service = ReBalanceService(db)
    re_balance = await re_balance_service.create(payload)
    return re_balance


@router.post("/sip", status_code=status.HTTP_201_CREATED)
async def sip_re_balance(payload: SIPReBalance, db: AsyncSession = Depends(get_db)):
    """ api to update re balance data. """
    re_balance_service = ReBalanceService(db)
    re_balance = await re_balance_service.sip_re_balance(payload)
    return re_balance

# @router.patch("/", status_code=status.HTTP_200_OK)
# async def update_re_balance(
#     payload: ReBalanceSchema, db: AsyncSession = Depends(get_db)
# ):
#     """ api to  re balance data. """
#     re_balance_service = ReBalanceService(db)
#     await re_balance_service.update(payload)


# @router.get("/{uuid}", status_code=status.HTTP_200_OK)
# async def get_re_balance(uuid: UUID, db: AsyncSession = Depends(get_db)):
#     """ api to get re balance data by id. """
#     re_balance_service = ReBalanceService(db)
#     re_balance = await re_balance_service.get_by_id(uuid)
#     return re_balance


# @router.get("/", status_code=status.HTTP_200_OK)
# async def get_re_balance(db: AsyncSession = Depends(get_db)):
#     """ api to get re balance data. """
#     re_balance_service = ReBalanceService(db)
#     re_balance = await re_balance_service.get_all()
#     return re_balance


# @router.delete("/{uuid}", status_code=status.HTTP_200_OK)
# async def delete_re_balance(uuid: UUID, db: AsyncSession = Depends(get_db)):
#     """ api to delete re balance data by id. """
#     re_balance_service = ReBalanceService(db)
#     await re_balance_service.delete(uuid)
