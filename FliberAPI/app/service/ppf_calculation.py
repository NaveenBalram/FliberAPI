import datetime
import logging
from uuid import UUID

from numpy_financial import fv
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.ppf_calculation import PpfCalculationRepository
from app.db.repositories.user import UserRepository
from app.models.schema.ppf_calculation import PpfCalculationSchema, InPpfCalculationSchema
from app.service.fv_formulae.fv import feature_value

logger = logging.getLogger(__name__)


class PpfCalculationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._ppf_calculation_repository = PpfCalculationRepository(self._db_session)

    async def create(self, payload: InPpfCalculationSchema):
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
        ppf_calculation = await self._ppf_calculation_repository.create(payload)

        return ppf_calculation

    async def get_by_id(self, uuid: UUID):
        ppf_calculation = await self._ppf_calculation_repository.get_by_id(uuid)
        return ppf_calculation

    async def get_all(self):
        ppf_calculation = await self._ppf_calculation_repository.get_all()
        return ppf_calculation

    async def delete(self, uuid: UUID):
        await self._ppf_calculation_repository.delete(uuid)

    async def update(self, payload: PpfCalculationSchema):
        await self._ppf_calculation_repository.update(payload)
