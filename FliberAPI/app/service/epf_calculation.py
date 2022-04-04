import datetime
import logging
from uuid import UUID

from numpy_financial import fv
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.epf_calculation import EpfCalculationRepository
from app.db.repositories.user import UserRepository
from app.models.schema.epf_calculation import EpfCalculationSchema, InEpfCalculationSchema
from app.service.fv_formulae.fv import feature_value

logger = logging.getLogger(__name__)


class EpfCalculationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._epf_calculation_repository = EpfCalculationRepository(self._db_session)

    async def create(self, payload: InEpfCalculationSchema):
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

        rc = feature_value(payload.YearlyContribution, payload.RateOfReturn, payload.InvestmentPeriod,
                           payload.GrowthRate)
        cb = fv(payload.RateOfReturn/100, nper, 0, -payload.AmountSavedSoFor, 1)

        total = rc["futureValue"] + cb

        return rc, total

        # epf_calculation = await self._epf_calculation_repository.create(payload)
        # return epf_calculation

    async def get_by_id(self, uuid: UUID):
        epf_calculation = await self._epf_calculation_repository.get_by_id(uuid)
        return epf_calculation

    async def get_all(self):
        epf_calculation = await self._epf_calculation_repository.get_all()
        return epf_calculation

    async def delete(self, uuid: UUID):
        await self._epf_calculation_repository.delete(uuid)

    async def update(self, payload: EpfCalculationSchema):
        await self._epf_calculation_repository.update(payload)
