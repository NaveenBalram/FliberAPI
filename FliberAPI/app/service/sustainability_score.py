import datetime
import logging
from uuid import UUID

import numpy as np
import numpy_financial as npf
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.retirement_status import RetirementStatusRepository
from app.db.repositories.submit_question import SubmitQuestionRepository
from app.db.repositories.sustainability_score import SustainabilityScoreRepository
from app.db.repositories.sustainability_score_configuration import SustainabilityScoreConfigurationRepository
from app.db.repositories.user import UserRepository
from app.models.schema.sustainability_score import OutSustainabilityScoreSchema, SustainabilityScoreSchema, \
    InSustainabilityScoreSchema

logger = logging.getLogger(__name__)


class SustainabilityScoreService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._sustainability_score_repository = SustainabilityScoreRepository(self._db_session)

    async def create(self, payload: InSustainabilityScoreSchema):
        sustainability_score = await self._sustainability_score_repository.create(payload)

        return sustainability_score

    async def sustainability_score(self, user_id: UUID, module_type: int):
        """ calculate the sustainability score for the user. """

        sustainability_repository = SustainabilityScoreConfigurationRepository(
            self._db_session
        )
        sa_score = await sustainability_repository.get_configurations()
        config = sa_score[0].__dict__

        retirement_age = config.get("RetirementAge")
        inflation = config.get("Inflation")
        life_exp = config.get("LifeExp")
        rateofReturn = config.get("RateOfReturn")

        current_user = user_id
        mt = module_type
        user_repository = UserRepository(self._db_session)
        dob = await user_repository.get_dob(user_id)
        retirement_repository = RetirementStatusRepository(self._db_session)
        retirementStatus = await retirement_repository.get_status(user_id)
        today = datetime.date.today()
        userAge = (
                today.year
                - dob[0].year
                - ((today.month, today.day) < (dob[0].month, dob[0].day))
        )
        answer_repository = SubmitQuestionRepository(self._db_session)

        user_retirement_status = retirementStatus[0]
        duration = life_exp - int(userAge)

        if user_retirement_status == 2:
            averageRetirementCorpus = await answer_repository.get_by_value(
                {
                    "QuestionId": UUID("5e4eec24-e56f-4a89-b83c-2b9f4cf1762d"),
                    "ModuleType": mt,
                    "UserId": current_user,
                }
            )
            try:
                if averageRetirementCorpus[0]:
                    averageRetirementCorpus = averageRetirementCorpus[0]
            except Exception as IndexError:
                return {
                    "error": str(IndexError),
                    "details": "AverageRetirementCorpus is not provided.",
                }

            MonthlyHouseholdExpense = await answer_repository.get_by_value(
                {
                    "QuestionId": UUID("89b57579-182f-4d37-b4b4-a004fa49fabd"),
                    "ModuleType": mt,
                    "UserId": current_user,
                }
            )
            try:
                if MonthlyHouseholdExpense[0]:
                    MonthlyHouseholdExpense = MonthlyHouseholdExpense[0]
            except Exception as IndexError:
                return {
                    "error": str(IndexError),
                    "details": "MonthlyHouseholdExpense is not provided.",
                }

            MonthlyHealthcareExpense = await answer_repository.get_by_value(
                {
                    "QuestionId": UUID("2d0cf406-0ff7-4f97-848b-b75caac4a61b"),
                    "ModuleType": mt,
                    "UserId": current_user,
                }
            )
            try:
                if MonthlyHealthcareExpense[0]:
                    MonthlyHealthcareExpense = MonthlyHealthcareExpense[0]
            except Exception as IndexError:
                return {
                    "error": str(IndexError),
                    "details": "MonthlyHealthcareExpense is not provided.",
                }

            postRetirementyearlyIncome = await answer_repository.get_by_value(
                {
                    "QuestionId": UUID("b8efe122-2793-4195-87ff-9a9f01f73720"),
                    "ModuleType": mt,
                    "UserId": current_user,
                }
            )

            try:
                if postRetirementyearlyIncome[0]:
                    postRetirementyearlyIncome = postRetirementyearlyIncome[0]
            except Exception as IndexError:
                return {
                    "error": str(IndexError),
                    "details": "postRetirementyearlyIncome is not provided.",
                }

            realRate = (rateofReturn - inflation) / (1 + inflation)
            realRate = round(realRate, 4)

            pvforhousehold = np.absolute(
                np.round_(
                    (
                        npf.pv(
                            realRate, duration, int(MonthlyHouseholdExpense) * 12, 0, 1
                        )
                    ),
                    decimals=5,
                )
            )

            pvforhealthcare = np.absolute(
                np.round_(
                    (
                        npf.pv(
                            realRate, duration, int(MonthlyHealthcareExpense) * 12, 0, 1
                        )
                    ),
                    decimals=5,
                )
            )

            pvforpostRetirementyearlyIncome = np.absolute(
                np.round_(
                    (npf.pv(realRate, duration, int(postRetirementyearlyIncome), 0, 1)),
                    decimals=5,
                )
            )

            totalpvofExpenses = np.sum([pvforhousehold, pvforhealthcare])
            effectiveCorpus = (
                    int(averageRetirementCorpus) - pvforpostRetirementyearlyIncome
            )
            sustainabilityRatio = totalpvofExpenses / effectiveCorpus

            return {"sustainabilityRatio": sustainabilityRatio}
        else:
            return {"msg": "User is not post retire"}

    async def get_by_id(self, uuid: UUID) -> OutSustainabilityScoreSchema:
        sustainability_score = await self._sustainability_score_repository.get_by_id(uuid)
        return sustainability_score

    async def get_all(self):
        sustainability_score = await self._sustainability_score_repository.get_all()
        return sustainability_score

    async def delete(self, uuid: UUID):
        await self._sustainability_score_repository.delete(uuid)

    async def update(self, payload: SustainabilityScoreSchema):
        await self._sustainability_score_repository.update(payload)
