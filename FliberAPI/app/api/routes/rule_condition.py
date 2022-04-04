import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.rule_condition import (
    OutRuleConditionSchema,
    InRuleConditionSchema,
    RuleConditionSchema
)
from app.service.rule_condition import RuleCondition

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_rule_condition(
    payload: InRuleConditionSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save rule condition data. """
    rule_condition_service = RuleCondition(db)
    rule_condition_service = await rule_condition_service.create(payload)
    return rule_condition_service


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_rule_condition(
    payload:RuleConditionSchema , db: AsyncSession = Depends(get_db)
):
    """ api to update funds type data. """
    rule_condition_service = RuleCondition(db)
    await rule_condition_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_rule_condition_by_id(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to fetch all fund category data. """
    rule_condition_service = RuleCondition(db)
    rule_condition_service = await rule_condition_service.get_by_id(uuid)
    return rule_condition_service


@router.get("/", status_code=status.HTTP_200_OK)
async def get_rule_condition(db: AsyncSession = Depends(get_db)):
    """ api to fetch all rule condition data. """
    rule_condition_service = RuleCondition(db)
    rule_condition_service = await rule_condition_service.get_all()
    return rule_condition_service


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_rule_condition(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to Fetch data by id. """
    rule_condition_service = RuleCondition(db)
    return await rule_condition_service.delete(uuid)

