
def feature_value(intial_investment: float, interest_rate: float, investment_period: int, growth_rate: float):
    cal = ((1 + interest_rate / 100) ** investment_period - (1 + growth_rate / 100) ** investment_period) / (
            (interest_rate / 100) - (growth_rate / 100))
    fv = intial_investment * cal * (1 + interest_rate / 100)
    return {"futureValue": round(fv, 2)}