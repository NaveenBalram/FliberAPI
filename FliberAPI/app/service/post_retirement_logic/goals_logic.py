import numpy_financial as npf
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.frequency import FrequencyRepository
from app.db.repositories.goal_category import GoalCategoryRepository


class Goals:

    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session

    async def generate_goals(self, user_goals, ret_age, exp_age, dataframe):
        """ method to calculate the fv/pv for the goals data. """

        r = exp_age - ret_age
        goal_names = []

        for goal in user_goals:

            goal_name = (
                goal.GoalCategoryName if goal.GoalCategoryName else goal.GoalName
            )
            goal_amount = goal.GoalAmount
            goal_rate = goal.GoalInflationRate
            goal_type = goal.GoalTypeName
            goal_names.append(goal_name)
            if goal_amount == 0:
                dataframe[goal_name] = [0 for i in range(r)]
                continue
            grate = 0

            goal_category_repository = GoalCategoryRepository(self._db_session)

            if goal_rate:
                grate = goal_rate / 100

            elif goal_name == "Others" or (
                    goal_type == "Adhoc" and not goal.GoalAmountType
            ):
                # get the default rate for the goals if goal name is others or adhoc
                grate = await goal_category_repository.get_by_name(
                    {"Name": "Household expenses"}
                )

                grate = grate[0] / 100

            elif goal_type not in ["Adhoc"]:
                # get the default rate for the goals if goal rate is not provided
                grate = await goal_category_repository.get_by_name(
                    {"Name": goal_name}
                )

                grate = grate[0] / 10

            frequency = 1

            frequency_repository = FrequencyRepository(self._db_session)

            frequency = await frequency_repository.get_by_name(
                {"Name": goal.FrequencyName}
            )
            frequency = frequency[0] / 100

            # negative amount is required to get positive value from fv
            amount = -(goal_amount * frequency)

            goal_start = goal.GoalStartAge
            goal_end = goal.GoalEndAge
            if goal_start:

                if goal_end:
                    # If goal requirement is for limited period, find the future value for the given start to end age.
                    age_range = [y for y in range(goal_start, goal_end + 1)]

                    if not goal.GoalAmountType:
                        at = ret_age
                    else:
                        at = goal_start

                    dataframe[goal_name] = [
                        round(npf.fv(grate, i - at, 0, amount, 1), 4)
                        if i in age_range
                        else 0
                        for i in range(ret_age, exp_age)
                    ]

                else:
                    # if goal amount is adhoc and if goal amount type is future value, find the future value,
                    # goal amount type is false for future value

                    if goal_type == "Adhoc" and not goal.GoalAmountType:
                        dataframe[goal_name] = [
                            round(npf.fv(grate, i - ret_age, 0, amount, 1), 4)
                            if i == goal_start
                            else 0
                            for i in range(ret_age, exp_age)
                        ]
                    else:

                        dataframe[goal_name] = [
                            goal_amount if i == goal_start else 0
                            for i in range(ret_age, exp_age)
                        ]

            else:
                dataframe[goal_name] = [
                    round(npf.fv(grate, i, 0, amount, 1), 4) for i in range(r)
                ]

        return goal_names
