import logging
import time
from uuid import UUID

import numpy_financial as npf
import pandas as pd
from numpy_financial import npv
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.generated_cash_ladder_pre import (
    GeneratedCashLadderPreRepository,
)
from app.db.repositories.generated_goals import GeneratedGoalsRepository
from app.db.repositories.pre_retirement_configuration import (
    PreRetirementConfigurationRepository,
)
from app.db.repositories.pre_retirement_corpus_calculation import (
    PreRetirementCorpusCalculationRepository,
)
from app.models.schema.generated_cash_ladder_pre import GeneratedCashLadderPreSchemaBase
from app.models.schema.generated_goals import GeneratedGoalsSchemaBase
from app.models.schema.pre_retirement_corpus_calculation import (
    InPreRetirementCorpusCalculationSchema,
    PreRetirementCorpusCalculationSchema,
    PreRetirementCorpusCalculationSchemaBase,
)

logger = logging.getLogger(__name__)


class PreRetirementCorpusCalculationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._pre_retirement_corpus_calculation_repository = PreRetirementCorpusCalculationRepository(self._db_session)
        self.pre_retirement_corpus_calculation_repository = (
            PreRetirementCorpusCalculationRepository(self._db_session)
        )

    async def create(
            self, payload: InPreRetirementCorpusCalculationSchema
    ):

        pre_retirement_corpus_calculation = (
            await self._pre_retirement_corpus_calculation_repository.create(payload)
        )

        return pre_retirement_corpus_calculation

    async def get_by_id(self, uuid: UUID):

        pre_retirement_corpus_calculation = (
            await self._pre_retirement_corpus_calculation_repository.get_by_id(uuid)
        )
        return pre_retirement_corpus_calculation

    async def get_all(self):

        pre_retirement_corpus_calculation = (
            await self._pre_retirement_corpus_calculation_repository.get_all()
        )
        return pre_retirement_corpus_calculation

    async def delete(self, uuid: UUID):

        await self._pre_retirement_corpus_calculation_repository.delete(uuid)

    async def update(self, payload: PreRetirementCorpusCalculationSchema):

        await self._pre_retirement_corpus_calculation_repository.update(payload)

    async def corpus_calculation(
            self, payload: PreRetirementCorpusCalculationSchemaBase
    ):
        # self.pre_retirement_corpus_calculation_repository
        pre_requirement_configuration = PreRetirementConfigurationRepository(
            self._db_session
        )
        data = payload.dict()
        current_user = data["UserId"]
        request = await pre_requirement_configuration.get_by_user_id(current_user)

        avg_monthly_expense = data["AvgMonthlyExpense"]
        avg_monthly_income = data["AvgMonthlyIncome"]
        avg_health_expense = data["AvgHealthExpense"]
        vacation_cost = request.data["VacationCost"]
        charity_planned_yearly = request.data["CharityPlannedYearly"]
        adhoc_income_yearly = request.data["AdhocIncome"]
        goals = request.data["Goals"]
        vacation_planned_from = request.data["VacationPlannedFrom"]
        vacation_planned_till = request.data["VacationPlannedTill"]
        currentage = request.data["CurrentAge"]

        config = await pre_requirement_configuration.get_by_user_id(current_user)
        retirement_age = config.get("RetirementAge")
        life_exp = config.get("LifeExp")
        calculation_limit_set = config.get("CalculationLimit")
        inflation = config.get("Inflation")
        health_care_inflation = config.get("HealthCareInflation")
        vacation_inflation = config.get("VacationInflation")
        discounting_rate = config.get("DiscountingRate:")
        asis = config.get("AsIs")
        luxury = config.get("Luxury")
        modest = config.get("Modest")
        growth_of_income_rate = config.get("GrowthFfIncomeRate")

        i_rate = inflation / 100
        h_rate = health_care_inflation / 100
        v_rate = vacation_inflation / 100
        d_rate = discounting_rate / 100
        asis_rate = asis / 100
        luxury_rate = luxury / 100
        modest_rate = modest / 100
        income_rate = growth_of_income_rate / 100

        duration = retirement_age - currentage
        calulationlimit = int(calculation_limit_set) + 1
        rangeval = int(calulationlimit) - (int(retirement_age) + 1)

        expense_at_asis = pd.DataFrame(
            {
                "expense_at_asis": [
                    int(
                        npf.fv(
                            i_rate,
                            duration + i,
                            0,
                            -(avg_monthly_expense + (avg_monthly_expense * asis_rate)),
                        )
                        * 12
                    )
                    for i in range(rangeval)
                ]
            },
            index=[i for i in range(retirement_age + 1, calulationlimit)],
        )

        expense_at_luxury = pd.DataFrame(
            {
                "expense_at_luxury": [
                    int(
                        npf.fv(
                            i_rate,
                            duration + i,
                            0,
                            -(
                                    avg_monthly_expense
                                    + (avg_monthly_expense * luxury_rate)
                            ),
                        )
                        * 12
                    )
                    for i in range(rangeval)
                ]
            },
            index=[i for i in range(retirement_age + 1, calulationlimit)],
        )

        expense_at_modest = pd.DataFrame(
            {
                "expense_at_modest": [
                    int(
                        npf.fv(
                            i_rate,
                            duration + i,
                            0,
                            -(
                                    avg_monthly_expense
                                    + (avg_monthly_expense * modest_rate)
                            ),
                        )
                        * 12
                    )
                    for i in range(rangeval)
                ],
            },
            index=[i for i in range(retirement_age + 1, calulationlimit)],
        )

        other = pd.DataFrame(
            {
                "health_care_expense": [
                    int(npf.fv(h_rate, i, 0, -avg_health_expense))
                    for i in range(rangeval)
                ],
                "charity": [charity_planned_yearly] * rangeval,
            },
            index=[i for i in range(retirement_age + 1, calulationlimit)],
        )

        value = [y for y in range(vacation_planned_from, vacation_planned_till + 1)]
        vacation_expense = pd.DataFrame(
            {
                "vacation_expense": [
                    int(npf.fv(v_rate, i - int(currentage), 0, -vacation_cost))
                    if i in value
                    else 0
                    for i in range(retirement_age + 1, calulationlimit)
                ]
            },
            index=[i for i in range(retirement_age + 1, calulationlimit)],
        )

        goal = pd.DataFrame(
            {}, index=[i for i in range(retirement_age + 1, calulationlimit)]
        )
        for x in goals:
            col = x.get("name")
            entry = [
                x.get("value") if i == ((x.get("atage") - retirement_age) - 1) else 0
                for i in range(rangeval)
            ]
            goal[col] = entry

        income = pd.DataFrame(
            {
                "regular_income": [
                    int(npf.fv(income_rate, i, 0, -avg_monthly_income) * 12)
                    for i in range(rangeval)
                ]
            },
            index=[i for i in range(retirement_age + 1, calulationlimit)],
        )

        adhoc_income = pd.DataFrame(
            {
                "adhoc_income": [
                    adhoc_income_yearly[str(i)]
                    if str(i) in adhoc_income_yearly.keys()
                    else 0
                    for i in range(retirement_age + 1, calulationlimit)
                ]
            },
            index=[i for i in range(retirement_age + 1, calulationlimit)],
        )

        yearly_income = pd.DataFrame(
            {
                "yearly_income": [
                    int(npf.fv(income_rate, i, 0, -avg_monthly_income) * 12)
                    for i in range(rangeval)
                ],
            },
            index=[i for i in range(retirement_age + 1, calulationlimit)],
        )
        for i in list(adhoc_income_yearly.keys()):
            yearly_income.at[int(i), "yearly_income"] = int(
                income._get_value(int(i), "regular_income")
            ) + int(adhoc_income_yearly.get(str(i)))

        userId = pd.DataFrame(
            {"userId": [current_user for i in range(rangeval)]},
            index=[i for i in range(retirement_age + 1, calulationlimit)],
        )

        age = pd.DataFrame(
            {"age": [age for age in range(retirement_age + 1, calulationlimit)]},
            index=[i for i in range(retirement_age + 1, calulationlimit)],
        )
        ###########################################################################
        goalsdata = [goal, userId, age]
        goalvalue = pd.concat(goalsdata, axis=1)
        my_list = list(goal)
        bulk_goals = []
        for col in my_list:

            selection = goalvalue[[col, "userId", "age"]]
            for i, frames in selection[["userId", "age", col]].iterrows():
                bulk_goals.append(
                    GeneratedGoalsSchemaBase(
                        UserId=frames["userId"],
                        Age=frames["age"],
                        GoalName=col,
                        GoalValue=frames[col],
                        GoalatAge=frames["age"],
                    )
                )
            generate_goals_repository = GeneratedGoalsRepository(self._db_session)
            await generate_goals_repository.bulk_insert(bulk_goals)
            ###########################################################################

        total = [
            userId,
            expense_at_asis,
            expense_at_luxury,
            expense_at_modest,
            other,
            vacation_expense,
            age,
            goal,
            income,
            adhoc_income,
            yearly_income,
        ]
        data = pd.concat(total, axis=1)

        as_is = [expense_at_asis, other, vacation_expense, goal]
        as_is = pd.concat(as_is, axis=1)
        data["yearly_expense_asis"] = as_is.sum(axis=1)

        luxury = [expense_at_luxury, other, vacation_expense, goal]
        luxury = pd.concat(luxury, axis=1)
        data["yearly_expense_luxury"] = luxury.sum(axis=1)

        modest = [expense_at_modest, other, vacation_expense, goal]
        modest = pd.concat(modest, axis=1)
        data["yearly_expense_modest"] = modest.sum(axis=1)

        data["net_expense_asis"] = data["yearly_expense_asis"].sub(
            yearly_income["yearly_income"], axis=0
        )
        data["net_expense_luxury"] = data["yearly_expense_luxury"].sub(
            yearly_income["yearly_income"], axis=0
        )
        data["net_expense_modest"] = data["yearly_expense_modest"].sub(
            yearly_income["yearly_income"], axis=0
        )

        retirement_corpus_asis = data["net_expense_asis"].iloc[0] + [
            npv(
                d_rate,
                data["net_expense_asis"].iloc[
                    [i for i in range(1, (life_exp - (retirement_age + 1)) + 1)]
                ],
            )
        ]
        retirement_corpus_luxury = data["net_expense_luxury"].iloc[0] + [
            npv(
                d_rate,
                data["net_expense_luxury"].iloc[
                    [i for i in range(1, (life_exp - (retirement_age + 1)) + 1)]
                ],
            )
        ]
        retirement_corpus_modest = data["net_expense_modest"].iloc[0] + [
            npv(
                d_rate,
                data["net_expense_modest"].iloc[
                    [i for i in range(1, (life_exp - (retirement_age + 1)) + 1)]
                ],
            )
        ]
        #################################################################
        # alchemyEngine = create_engine('postgresql://postgres:postgres@localhost/FliberV0.2', pool_recycle=3600)
        # postgreSQLConnection = alchemyEngine.connect()
        postgreSQLTable = "Preretirementcorpus"
        start_time = time.time()
        try:
            data.to_sql(
                postgreSQLTable,
                self._db_session,
                if_exists="replace",
                index_label="age",
            )
            print("to_sql duration:{} seconds".format(time.time() - start_time))
        except ValueError as vx:
            print(vx)
        except Exception as ex:
            print(ex)
        else:
            print(
                "PostgreSQL Table %s has been created successfully." % postgreSQLTable
            )

        #################################################################
        result = []
        for i, frames in data[
            [
                "userId",
                "age",
                "expense_at_asis",
                "expense_at_luxury",
                "expense_at_modest",
                "health_care_expense",
                "vacation_expense",
                "charity",
                "regular_income",
                "adhoc_income",
                "yearly_income",
                "yearly_expense_asis",
                "yearly_expense_luxury",
                "yearly_expense_modest",
                "net_expense_asis",
                "net_expense_luxury",
                "net_expense_modest",
            ]
        ].iterrows():
            result.append(
                GeneratedCashLadderPreSchemaBase(
                    UserId=frames["userId"],
                    Age=frames["age"],
                    ExpenseAtAsIs=frames["expense_at_asis"],
                    ExpenseAtLuxury=frames["expense_at_luxury"],
                    ExpenseAtModest=frames["expense_at_modest"],
                    HealthCareExpense=frames["health_care_expense"],
                    VacationExpense=frames["vacation_expense"],
                    Charity=frames["charity"],
                    Income=frames["regular_income"],
                    AdhocIncome=frames["adhoc_income"],
                    YearlyIncome=frames["yearly_income"],
                    YearlyExpenseAsIs=frames["yearly_expense_asis"],
                    YearlyExpenseLuxury=frames["yearly_expense_luxury"],
                    YearlyExpenseModest=frames["yearly_expense_modest"],
                    NetExpenseAsIs=frames["net_expense_asis"],
                    NetExpenseLuxury=frames["net_expense_luxury"],
                    NetExpenseModest=frames["net_expense_modest"],
                )
            )

        generaterd_cash_ladder = GeneratedCashLadderPreRepository(self._db_session)
        await generaterd_cash_ladder.bulk_insert(result)

        data.to_excel("output3.xlsx", sheet_name="sheet 1", index=0)

        return {
            "retirement_corpus": {
                "asis": retirement_corpus_asis[0],
                "luxury": retirement_corpus_luxury[0],
                "modest": retirement_corpus_modest[0],
            }
        }
