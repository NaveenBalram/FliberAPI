import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.policy_weightage import (
    OutPolicyWeightageSchema,
    InPolicyWeightageSchema,
    PolicyWeightageSchema,
)
from app.service.policy_weightage import PolicyWeightageService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutPolicyWeightageSchema
)
async def create_policy_weightage(
    payload: InPolicyWeightageSchema, db: AsyncSession = Depends(get_db)
) -> OutPolicyWeightageSchema:
    """ api to save policy weightage data. """
    policy_weightage_service = PolicyWeightageService(db)
    policy_weightage = await policy_weightage_service.create(payload)
    return policy_weightage


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_policy_weightage(
    payload: PolicyWeightageSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update policy weightage data. """
    policy_weightage_service = PolicyWeightageService(db)
    await policy_weightage_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutPolicyWeightageSchema
)
async def get_policy_weightage(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutPolicyWeightageSchema:
    """ api to get policy weightage data by id. """
    policy_weightage_service = PolicyWeightageService(db)
    policy_weightage = await policy_weightage_service.get_by_id(uuid)
    return policy_weightage


@router.get("/", status_code=status.HTTP_200_OK)
async def get_policy_weightage(db: AsyncSession = Depends(get_db)):
    """ api to get policy weightage data. """
    policy_weightage_service = PolicyWeightageService(db)
    policy_weightage = await policy_weightage_service.get_all()
    return policy_weightage


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_policy_weightage(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete policy weightage data by id. """
    policy_weightage_service = PolicyWeightageService(db)
    await policy_weightage_service.delete(uuid)


# @router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
# async def delete_policy_weightage_by_user_id(
#     user_id: UUID, db: AsyncSession = Depends(get_db)
# ):
#     """ api to  policy weightage data. """
#     policy_weightage_service = PolicyWeightageService(db)
#     await policy_weightage_service.delete(user_id)
