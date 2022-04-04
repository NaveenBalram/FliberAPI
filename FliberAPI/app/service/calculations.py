import datetime
import logging
from copy import deepcopy
from operator import itemgetter
from uuid import UUID

import numpy as np
import numpy_financial as npf
import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from app.db.repositories.ability_configuration import AbilityConfigurationRepository
from app.db.repositories.generated_buckets import GeneratedBucketsRepository
from app.db.repositories.generated_cash_ladder import GeneratedCashLadderRepository
from app.db.repositories.generated_goals import GeneratedGoalsRepository
from app.db.repositories.generated_incomes import GeneratedIncomesRepository
from app.db.repositories.post_retirement_configuration import (
    PostRetirementConfigurationRepository,
)
from app.db.repositories.question import QuestionRepository
from app.db.repositories.question_type import QuestionTypeRepository
from app.db.repositories.retirement_status import RetirementStatusRepository
from app.db.repositories.risk_profile_configuration import (
    RiskProfileConfigurationRepository,
)
from app.db.repositories.rr_score_configuration import RrScoreConfigurationRepository
from app.db.repositories.rr_score_result import RrScoreResultRepository
from app.db.repositories.submit_question import SubmitQuestionRepository
from app.db.repositories.sustainability_score_configuration import (
    SustainabilityScoreConfigurationRepository,
)
from app.db.repositories.user import UserRepository
from app.db.repositories.user_goals import UserGoalsRepository
from app.db.repositories.user_incomes import UserIncomesRepository
from app.db.repositories.user_result import UserResultRepository
from app.db.repositories.willingness_configuration import (
    WillingnessConfigurationRepository,
)
from app.models.schema.rr_score_result import RrScoreResultSchemaBase
from app.service.post_retirement_logic.cash_ladder import CashLadder

logger = logging.getLogger(__name__)


class CalculationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session

    async def get_risk_profile_calculation(self, user_id: UUID, module_type: int):
        """Function to calculate the risk profile.

        variables: user_id, module_type.
        returns: risk profile or error.
        """

        # initiating the QuestionTypeRepository.
        question_type_repository = QuestionTypeRepository(self._db_session)

        # initiating the SubmitQuestionRepository.
        answer_repository = SubmitQuestionRepository(self._db_session)

        # initiating the AbilityConfigurationRepository.
        ability_repository = AbilityConfigurationRepository(self._db_session)

        # Fetching the id of type "Ability" from QuestionType table.
        ab = await question_type_repository.get_by_name(name="Ability")

        # Fetching the ability score based on the answers.
        ab_score = await answer_repository.get_by_value(
            {"QuestionId": ab[0], "ModuleType": module_type, "UserId": user_id}
        )

        if ab_score[0]:
            # Fetching the ability type based on the score .
            ab_type = await ability_repository.get_ability_type(ab_score[0])
        else:
            return f"The ability score is {ab_score}"

        # initiating the WillingnessConfigurationRepository.
        willingness_repository = WillingnessConfigurationRepository(self._db_session)

        # Fetching the id of type "Willingness" from QuestionType table.
        wi = await question_type_repository.get_by_name(name="Willingness")

        # Fetching the willingness score based on the answers.
        wi_score = await answer_repository.get_by_value(
            {"QuestionId": wi[0], "ModuleType": module_type, "UserId": user_id}
        )

        wi_type = await willingness_repository.get_willingness_type(wi_score[0])

        rp_repository = RiskProfileConfigurationRepository(self._db_session)
        rp = await rp_repository.get_risk_profile(ab_type.Type)

        rp = rp[0].__dict__

        risk_profile = rp[wi_type.Type]
        user_result_repository = UserResultRepository(self._db_session)
        await user_result_repository.update_result(risk_profile, str(user_id))
        return risk_profile

    async def get_rr_score_calculation(
            self, user_id: UUID, module_type: int, r_age: int
    ):
        rr_score_repository = RrScoreConfigurationRepository(self._db_session)
        configs = await rr_score_repository.get_configurations()

        question_type_repository = QuestionTypeRepository(self._db_session)
        question_type = await question_type_repository.get_by_name("RRScore")

        questions_repository = QuestionRepository(self._db_session)
        questions = await questions_repository.get_by_question_type(question_type[0])
        questions = dict((data[1], data[0]) for data in questions)

        CONFIG = configs[0].__dict__

        RORforEPFOandGS = CONFIG.get("RORforEPFOAndGS") / 100
        EquityRORforNPSandMLI = CONFIG.get("EquityRORforNPSandMLI") / 100
        DebtORforNPSandMLI = CONFIG.get("DebtORforNPSandMLI") / 100
        InflationRate = CONFIG.get("InflationRate") / 100
        RateofReturn = CONFIG.get("RateOfReturn") / 100
        life_exp = CONFIG.get("LifeExp")  # or date_config.get("LifeExpectancy")
        retirement_age = CONFIG.get(
            "RetirementAge"
        )  # or date_config.get("RetirementAge")

        mt = module_type
        current_user = user_id
        retirement_age_by_user = r_age

        user_repository = UserRepository(self._db_session)
        dob = await user_repository.get_dob(user_id)

        today = datetime.datetime.now().today()
        # get user age from date of birth
        userAge = (
                today.year
                - dob[0].year
                - ((today.month, today.day) < (dob[0].month, dob[0].day))
        )

        answer_repository = SubmitQuestionRepository(self._db_session)

        if retirement_age == retirement_age_by_user or retirement_age_by_user == 0:
            duration = retirement_age - int(userAge)
        else:
            duration = retirement_age_by_user - int(userAge)
        months = 12

        durationforPV = life_exp - retirement_age_by_user if retirement_age_by_user else retirement_age

        totalEPFOandGSBalance = await answer_repository.get_by_value(
            {
                "QuestionId": questions[2],
                "ModuleType": mt,
                "UserId": current_user,
            }
        )

        if totalEPFOandGSBalance:
            totalEPFOandGSBalance = int(totalEPFOandGSBalance[0])
        else:
            totalEPFOandGSBalance = 0

        yearlyEFPOandGSBalance = await answer_repository.get_by_value(
            {
                "QuestionId": questions[3],
                "ModuleType": mt,
                "UserId": current_user,
            }
        )

        if yearlyEFPOandGSBalance:
            yearlyEFPOandGSBalance = int(yearlyEFPOandGSBalance[0])
        else:
            yearlyEFPOandGSBalance = 0

        FVEofEPFOandGS = npf.fv(
            float(RORforEPFOandGS),
            duration,
            int(yearlyEFPOandGSBalance),
            int(totalEPFOandGSBalance),
            1,
        )

        totalNPSandMLIBalance = await answer_repository.get_by_value(
            {
                "QuestionId": questions[4],
                "ModuleType": mt,
                "UserId": current_user,
            }
        )

        if totalNPSandMLIBalance:
            totalNPSandMLIBalance = int(totalNPSandMLIBalance[0])
        else:
            totalNPSandMLIBalance = 0

        yearlyNPSandMLIBalance = await answer_repository.get_by_value(
            {
                "QuestionId": questions[5],
                "ModuleType": mt,
                "UserId": current_user,
            }
        )
        if yearlyNPSandMLIBalance:
            yearlyNPSandMLIBalance = int(yearlyNPSandMLIBalance[0])
        else:
            yearlyNPSandMLIBalance = 0

        EquityforNPSandMLI = await answer_repository.get_by_value(
            {
                "QuestionId": questions[6],
                "ModuleType": mt,
                "UserId": current_user,
            }
        )

        if EquityforNPSandMLI:
            EquityforNPSandMLI = int(EquityforNPSandMLI[0])
        else:
            EquityforNPSandMLI = 0

        finalEquityforNPSandMLI = float(EquityforNPSandMLI) / 100
        finalDebtforNPSandMLI = (100 - float(EquityforNPSandMLI)) / 100

        totalEquityinNPSandMLI = float(totalNPSandMLIBalance) * finalEquityforNPSandMLI
        yearlyEqityinNPSandMLI = float(yearlyNPSandMLIBalance) * finalEquityforNPSandMLI
        totalDebtinNPSandMLI = float(totalNPSandMLIBalance) * finalDebtforNPSandMLI
        yearlyDebtinNPSandMLI = float(yearlyNPSandMLIBalance) * finalDebtforNPSandMLI

        FVEofNPSandMLIEquity = npf.fv(
            float(EquityRORforNPSandMLI),
            duration,
            float(yearlyEqityinNPSandMLI),
            float(totalEquityinNPSandMLI),
            1,
        )
        FVEofNPSandMLIDebt = npf.fv(
            float(DebtORforNPSandMLI),
            duration,
            float(yearlyDebtinNPSandMLI),
            float(totalDebtinNPSandMLI),
            1,
        )

        TFVNPSandMLI = np.sum([FVEofNPSandMLIEquity, FVEofNPSandMLIDebt])

        # FCA = np.absolute(np.round_((np.sum([FVEofEPFOandGS, TFVNPSandMLI])), decimals=4))

        FCA = np.absolute(np.round_(np.sum([FVEofEPFOandGS, TFVNPSandMLI])))

        ### Monthly Expenses ###

        monthlyExpenses = await answer_repository.get_by_value(
            {
                "QuestionId": questions[1],
                "ModuleType": mt,
                "UserId": current_user,
            }
        )

        if monthlyExpenses:
            monthlyExpenses = int(monthlyExpenses[0])
        else:
            monthlyExpenses = 0

        yearlyExpenses = float(monthlyExpenses) * months

        ###AmountRequiredAsperMonthlyExpenses############
        AmountRequired = np.absolute(
            np.round_((yearlyExpenses * (1 + InflationRate) ** duration), decimals=4)
        )

        ####RealRate###
        realRate = (RateofReturn - InflationRate) / (1 + InflationRate)

        ##### Presentvalue/COR ###
        COR = np.absolute(
            np.round_(
                (npf.pv(realRate, durationforPV, float(AmountRequired), 0, 1)),
                decimals=4,
            )
        )

        ##### RRScore ###
        RRScore = FCA / COR
        Shortfall = FCA - COR

        round_FCA = np.absolute(np.round_(FCA, decimals=4))
        percentage_125 = np.round_((125 / 100 * COR), decimals=4)
        percentage_100 = np.round_((100 / 100 * COR), decimals=4)
        percentage_90 = np.round_((90 / 100 * COR), decimals=4)
        percentage_75 = np.round_((75 / 100 * COR), decimals=4)

        result = {}
        if round_FCA >= percentage_125:
            result = {
                "RRScoreResult": "Excellent",
                "COR": COR,
                "FCA": FCA,
                "age": userAge,
                "AmountRequired": AmountRequired,
            }
        elif percentage_125 > round_FCA > percentage_100:
            result = {
                "RRScoreResult": "Very Good",
                "COR": COR,
                "FCA": FCA,
                "age": userAge,
                "AmountRequired": AmountRequired,
            }
        elif percentage_100 > round_FCA > percentage_90:
            result = {
                "RRScoreResult": "Good",
                "COR": COR,
                "FCA": FCA,
                "age": userAge,
                "AmountRequired": AmountRequired,
            }
        elif percentage_90 > round_FCA > percentage_75:
            result = {
                "RRScoreResult": "Fair",
                "COR": COR,
                "FCA": FCA,
                "age": userAge,
                "AmountRequired": AmountRequired,
            }
        else:
            result = {
                "RRScoreResult": "Need Attention",
                "COR": COR,
                "FCA": FCA,
                "age": userAge,
                "AmountRequired": AmountRequired,
            }

        payload = RrScoreResultSchemaBase(
            UserId=user_id,
            RRScoreResult=result["RRScoreResult"],
            CorpusRequired=result["COR"],
            ExpectedValueOfExistingInvestments=result["FCA"],
            UserAge=userAge,
            RetirementAge=retirement_age_by_user if retirement_age_by_user else retirement_age,
            AmountRequired=result["AmountRequired"],
            CreatedOn=datetime.datetime.now(),
            UpdatedOn=datetime.datetime.now(),
            IsDeleted=False
        )

        rr_score_result = RrScoreResultRepository(self._db_session)
        await rr_score_result.delete_by_user(user_id)
        await rr_score_result.create(payload)

        return result

    async def sustainability_score(self, user_id: UUID, module_type: int):

        sustainability_repository = SustainabilityScoreConfigurationRepository(
            self._db_session
        )
        sa_score = await sustainability_repository.get_configurations()
        config = sa_score[0].__dict__

        retirement_age = config.get("RetirementAge")
        inflation = config.get("Inflation")
        life_exp = config.get("LifeExp")
        # health_care_inflation = config.get('HealthCareInflation')
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
                raise ValueError("AverageRetirementCorpus is not provided.")

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
                raise ValueError("MonthlyHouseholdExpense is not provided.")

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
                raise ValueError("MonthlyHealthcareExpense is not provided.")

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
                raise ValueError("postRetirementYearlyIncome is not provided.")

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

    async def post_retirement(self, user_id: UUID, constraint: bool, amount: float):
        """ Method to perform post retirement calculations and optimization. """

        # fetch post retirement configuration data
        post_repository = PostRetirementConfigurationRepository(self._db_session)
        result = await post_repository.get_by_user(user_id)

        user_repository = UserRepository(self._db_session)
        # related_age = user_repository.get_related_age(user_id)

        payload = result[0]
        data = pd.DataFrame()

        r_age = payload.RetirementAge + 1
        le_age = payload.LifeExpectancy
        expected_age = le_age - r_age

        e_age = 101

        data["Age"] = [age for age in range(r_age, e_age)]

        # fetch named tuple and dict values for goals
        user_goals_repository = UserGoalsRepository(self._db_session)
        goals_fetched, goals_data = await user_goals_repository.fetch_user_goals(user_id)

        if not goals_fetched:
            return JSONResponse({"exception": "DataDoesNotExist", "error": "User goals is empty"}, status_code=400)

        # sort the goals according to the priority
        goals = sorted(goals_fetched, key=itemgetter("GoalPriority"))
        goals_data = sorted(goals_data, key=itemgetter("GoalPriority"))
        verify_goals = deepcopy(goals_data)

        # fetch income for the user
        income_repository = UserIncomesRepository(self._db_session)
        income = await income_repository.fetch_user_income(user_id)

        if not income:
            raise ValueError("User income is empty")

        corpus = payload.CorpusAmount

        index = 0
        goal_amount = {}
        length_of_goals = len(goals)
        cash_ladder = CashLadder(self._db_session)

        # if constraint is false do the post retirement calculation
        # if constraint is true do the optimization
        if not constraint:
            data = await cash_ladder.generate_cash_ladder(goals, income, r_age, e_age, data, corpus)
        else:
            # optimization logic
            while 1:
                if abs(index) >= length_of_goals:
                    break

                data = await cash_ladder.generate_cash_ladder(
                    goals, income, r_age, e_age, data, corpus
                )

                # check if the closing balance is equal to amount
                if not data["Closing Balance"].loc[0:expected_age].ge(amount).all():
                    index = index - 1
                    goal_amount[goals_data[index]["GoalPriority"]] = goals_data[index]["GoalAmount"]
                    goals_data[index]["GoalAmount"] = 0.0
                    continue

                check = True
                current_amount = 0
                prev_amount = 0
                count = 0
                check_index = index + 1

                if abs(index) <= length_of_goals:
                    while index < check_index:
                        count = count + 1

                        if goals_data[index]["GoalAmount"] == 0:
                            goals_data[index]["GoalAmount"] = goal_amount[goals_data[index]["GoalPriority"]]

                        if check:
                            if prev_amount == 0:
                                prev_amount = goals_data[index]["GoalAmount"]
                            else:
                                prev_amount = goals_data[index]["GoalAmount"]
                                goals_data[index]["GoalAmount"] = round(prev_amount / 2, 4)

                            if goals_data[index]["GoalAmount"] > 1:

                                data = await cash_ladder.generate_cash_ladder(
                                    goals, income, r_age, e_age, data, corpus
                                )

                                if (
                                        not data["Closing Balance"]
                                                    .loc[0:expected_age]
                                                .ge(amount)
                                                .all()
                                ):
                                    continue

                            else:
                                goals_data[index]["GoalAmount"] = 0
                                index = index + 1
                                continue

                        if current_amount == 0:
                            current_amount = goals_data[index]["GoalAmount"]

                        if goals_data[index]["GoalAmount"] != 0:
                            check = False
                            goals_data[index]["GoalAmount"] = round(
                                (prev_amount + current_amount) / 2, 4
                            )

                            if (
                                    goals_data[index]["GoalAmount"] <= current_amount
                                    or prev_amount == goals_data[index]["GoalAmount"]
                            ):
                                goals_data[index]["GoalAmount"] = (
                                    current_amount if current_amount > 2 else 0
                                )
                                index = index + 1
                                check = True
                                current_amount = 0
                                continue

                            data = await cash_ladder.generate_cash_ladder(
                                goals, income, r_age, e_age, data, corpus
                            )
                            if (
                                    not data["Closing Balance"]
                                                .loc[0:expected_age]
                                            .ge(amount)
                                            .all()
                            ):
                                prev_amount = goals_data[index]["GoalAmount"]
                                continue

                            current_amount = goals_data[index]["GoalAmount"]

        data.to_excel("output.xlsx", sheet_name="sheet 1", index=0)

        result = {}
        data.to_dict()

        # GeneratedCashLadder()
        # GeneratedGoals()
        # GeneratedIncomes()
        # GeneratedBuckets()

        cash_ladder_repository = GeneratedCashLadderRepository(self._db_session)
        generated_goals_repository = GeneratedGoalsRepository(self._db_session)
        generated_income_repository = GeneratedIncomesRepository(self._db_session)
        generated_buckets_repository = GeneratedBucketsRepository(self._db_session)
        await cash_ladder_repository.delete_cash_ladder_by_user_id(user_id)
        await generated_goals_repository.delete_goals_by_user_id(user_id)
        await generated_income_repository.delet_incomes_by_user_id(user_id)
        await generated_buckets_repository.delete_buckets_by_user_id(user_id)

        for i in range(len(verify_goals)):

            goal_name = (
                goals_data[i]["GoalCategoryName"]
                if goals_data[i]["GoalCategoryName"]
                else goals_data[i]["GoalName"]
            )
            if verify_goals[i]["GoalAmount"] == goals_data[i]["GoalAmount"]:
                result[goal_name] = "Satisfied"
            elif 0 < goals_data[i]["GoalAmount"] < verify_goals[i]["GoalAmount"]:
                result[goal_name] = "Partially Satisfied"
            elif goals_data[i]["GoalAmount"] == 0:
                result[goal_name] = "Not Satisfied"

            result[f"{goal_name}_amount"] = goals_data[i]["GoalAmount"]

        return result
