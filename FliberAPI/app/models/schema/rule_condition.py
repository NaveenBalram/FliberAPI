from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class RuleConditionSchemaBase(BaseSchema):
    Rulenumber: str
    RiskCategory: str
    FundingMinAmount: int
    FundingMaxAmount: int
    TimetoRetirementMin: int
    TimetoRetirementMax: int
    CreatedOn: datetime


class RuleConditionSchema(RuleConditionSchemaBase):
    Id: UUID


class InRuleConditionSchema(RuleConditionSchemaBase):
    ...


class OutRuleConditionSchema(RuleConditionSchema):
    ...
