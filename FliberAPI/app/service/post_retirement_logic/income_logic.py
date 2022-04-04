import numpy_financial as npf
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.frequency import FrequencyRepository
from app.db.repositories.income_category import IncomeCategoryRepository


class Income:

    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session

    async def generate_income(self, incomes, ret_age, exp_age, dataframe):
        """ method to generate fv/pv for income data"""
        r = exp_age - ret_age
        income_names = []

        for income in incomes:

            income_name = income.IncomeCategoryName
            income_amount = income.IncomeAmount
            income_rate = income.IncomeInflationRate
            income_type = income.IncomeTypeName

            if income_amount <= 0:
                raise ValueError(f"Amount not defined for {income.Name}")

            irate = 0

            income_category_repository = IncomeCategoryRepository(self._db_session)
            if income_rate:
                irate = income_rate / 100

            elif income_name == "Others" or (income_type == "Adhoc" and not income.IncomeAmountType):
                # if income rate is not given fetch default rate of income name "Pension".
                irate = await income_category_repository.get_by_name(
                    {"Name": "Pension"}
                )
                irate = irate[0] / 100

            elif income_type not in ["Adhoc", "adhoc"]:
                # if income rate is not given fetch default rate for the income
                irate = await income_category_repository.get_by_name(
                    {"Name": income_name}
                )
                irate = irate[0] / 100

            frequency_repository = FrequencyRepository(self._db_session)

            frequency = await frequency_repository.get_by_name(
                {"Name": income.FrequencyName}
            )
            frequency = frequency[0] / 100

            amount = -(income_amount * frequency)

            income_names.append(income_name)
            income_start = income.IncomeStartAge
            income_end = income.IncomeEndAge
            if income_start:

                if income_end:
                    age_range = [y for y in range(income_start, income_end + 1)]

                    if not income_end:
                        at = ret_age
                    else:
                        at = income_start

                    dataframe[income_name] = [
                        round(npf.fv(irate, i - at, 0, amount, 1), 4)
                        if i in age_range
                        else 0
                        for i in range(ret_age, exp_age)
                    ]

                else:

                    if income_type == "Adhoc" and not income.IncomeAmountType:
                        dataframe[income_name] = [
                            round(npf.fv(irate, i - ret_age, 0, amount, 1), 4)
                            if i == income_start
                            else 0
                            for i in range(ret_age, exp_age)
                        ]

                    else:
                        dataframe[income_name] = [
                            income_amount if i == income_start else 0
                            for i in range(ret_age, exp_age)
                        ]

            else:
                dataframe[income_name] = [
                    round(npf.fv(irate, i, 0, amount, 1), 4) for i in range(r)
                ]

        return income_names
