import datetime
import logging
from uuid import UUID

from numpy_financial import fv
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.bonds_calculation import BondsCalculationRepository
from app.db.repositories.financial_amount_calculation import FinancialAmountCalculationRepository
from app.db.repositories.financial_user_table import FinancialUserTableRepository
from app.db.repositories.user import UserRepository
from app.models.schema.bonds_calculation import BondsCalculationSchema, InBondsCalculationSchema
from app.models.schema.financial_amount_calculation import FinancialAmountCalculationSchema
from app.service.fv_formulae.fv import feature_value

logger = logging.getLogger(__name__)


class BondsCalculationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._bonds_calculation_repository = BondsCalculationRepository(self._db_session)

    async def create(self, payload: InBondsCalculationSchema):
        user_repository = UserRepository(self._db_session)
        user = await user_repository.get_related_age(payload.UserId)
        dob = await user_repository.get_dob(payload.UserId)

        today = datetime.date.today()
        userAge = (
                today.year
                - dob[0].year
                - ((today.month, today.day) < (dob[0].month, dob[0].day))
        )

        nper = user[0].RetirementAge - userAge

        cbe = fv(payload.ReturnOnInvestment / 100, nper, 0,
                 -payload.AmountSavedSoFor * (payload.EquityPercentage / 100), 1)
        cbd = fv(payload.ReturnOnInvestment / 100, nper, 0,
                 -payload.AmountSavedSoFor * (100 - payload.EquityPercentage / 100), 1)

        total_cb = cbe + cbd

        rce = feature_value(payload.YearlyContribution * (payload.EquityPercentage / 100), payload.ReturnOnInvestment,
                            payload.NumberOfYears,
                            payload.AnnualGrowthRate)

        rcd = feature_value(payload.YearlyContribution * (100 - payload.EquityPercentage / 100),
                            payload.ReturnOnInvestment, payload.NumberOfYears,
                            payload.AnnualGrowthRate)

        total_rc = rce + rcd

        total_fv = total_cb + total_rc

        financial_user_table_repository = FinancialUserTableRepository(self._db_session)
        financial_user_table_repository = await financial_user_table_repository.create(payload)

        financial_calculation = FinancialAmountCalculationRepository(self._db_session)
        payload = FinancialAmountCalculationSchema(
            UserId=payload.UserId,
            Type=payload.Type,
            Name=payload.Name,
            ToatalAmount=total_fv,
            CreatedOn=datetime.datetime.now(),
            UpdatedOn=datetime.datetime.now(),
            IsDeleted=payload.IsDeleted
        )
        await financial_calculation.create(payload)

        return total_fv

    async def get_by_id(self, uuid: UUID):
        bonds_calculation = await self._bonds_calculation_repository.get_by_id(uuid)
        return bonds_calculation

    async def get_all(self):
        bonds_calculation = await self._bonds_calculation_repository.get_all()
        return bonds_calculation

    async def delete(self, uuid: UUID):
        await self._bonds_calculation_repository.delete(uuid)

    async def update(self, payload: BondsCalculationSchema):
        await self._bonds_calculation_repository.update(payload)
