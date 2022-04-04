import datetime
import logging
from uuid import UUID

from numpy_financial import fv
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.nps_calculation import NpsCalculationRepository
from app.db.repositories.user import UserRepository
from app.models.schema.nps_calculation import NpsCalculationSchema, InNpsCalculationSchema
from app.service.fv_formulae.fv import feature_value

logger = logging.getLogger(__name__)


class NpsCalculationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._nps_calculation_repository = NpsCalculationRepository(self._db_session)

    async def create(self, payload: InNpsCalculationSchema):
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

        nps_calculation = await self._nps_calculation_repository.create(payload)

        return total_fv

    async def get_by_id(self, uuid: UUID):
        nps_calculation = await self._nps_calculation_repository.get_by_id(uuid)
        return nps_calculation

    async def get_all(self):
        nps_calculation = await self._nps_calculation_repository.get_all()
        return nps_calculation

    async def delete(self, uuid: UUID):
        await self._nps_calculation_repository.delete(uuid)

    async def update(self, payload: NpsCalculationSchema):
        await self._nps_calculation_repository.update(payload)
