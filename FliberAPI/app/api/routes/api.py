from fastapi import APIRouter

from app.api.routes import (
    gender,
    advisor,
    user,
    bucket,
    bank_account_type,
    marital_status,
    event_type,
    funds_category,
    funds_type,
    loan_type,
    income_type,
    instrument_type,
    relation_type,
    retirement_status,
    corpus_status,
    portfolio_morning_star,
    areas_of_concerns,
    asset_type,
    asset_allocation_attributes,
    asset_liability_category,
    policy_weightage,
    investment_type,
    investment_bucket,
    payment_type,
    investment_vehicle,
    investment_profile,
    role,
    question_type,
    question,
    choice,
    user_answers,
    user_result,
    rate,
    frequency,
    goal_type,
    other_goal_type,
    expense_type,
    goal_bucket,
    goal_category,
    expense_category,
    income_category,
    user_goals,
    user_incomes,
    generated_goals,
    generated_incomes,
    generated_cash_ladder,
    generated_buckets,
    submit_question,
    target_assets,
    post_goal,
    income,
    calculations,
    kyc,
    order,
    payment,
    bse_client_occupation_code,
    bse_country_code,
    bse_state_code,
    bse_client_tax_status,
    bse_account_type,
    bse_communication_mode,
    bse_pan_exempt_category,
    bse_income_slab,
    nominee_relation,
    occupation_types,
    source_of_wealth,
    bse_client_code,
    bse_client_nominee,
    banks,
    bank_branches,
    sign_zy,
    signzy_account,
    bse_client_account,
    refund,
    settlement,
    sustainability_score_configuration,
    ability_configuration,
    willingness_configuration,
    rr_score_configuration,
    risk_profile_configuration,
    pre_retirement_configuration,
    post_retirement_configuration,
    cash_free_configuration,
    pre_retirement_corpus_calculation,
    user_assets,
    users_re_balance_sheet,
    daily_asset_data,
    morning_star_navs,
    daily_nav_data,
    assets_limit,
    re_balance,
    fund_level_asset_percent,
    phone_api,
    sustainability_score,
    net_worth_investment_data,
    net_worth_other_asset_data,
    net_worth_bank_deposit_data,
    net_worth_fixed_deposit_data,
    net_worth_life_insurance_data,
    net_worth_house_data,
    net_worth_vehicle_data,
    net_worth_gold_data,
    net_worth_others_data,
    net_worth_stocks_data,
    net_worth_category_data,
    net_worth_bucket_data,
    net_worth_loan_type_data,
    net_worth_scheme_type_data,
    net_worth_vehicle_type_data,
    net_worth_frequency_type_data,
    net_worth_user_table_data,
    rr_score_result,
    rule_condition,
    epf_calculation,
    mf_calculation,
    nps_calculation,
    financial_amount_calculation,
    ppf_calculation,
    bonds_calculation,
    stocks_calculation,
    others_calculation,
    net_worth_calculation,
    rule_asset_allocation,
    asset_class_hierarchy,
    asset_advisory,
    cas_data_upload_from_pulse_lab,
    cas_data_upload_to_pulse_lab,
    epfo_auto_fetch,
    cas_upload
)

api_router = APIRouter()
api_router.include_router(
    calculations.router, prefix="/Calculations", tags=["Calculation"]
)
api_router.include_router(gender.router, prefix="/Gender", tags=["Gender"])
api_router.include_router(advisor.router, prefix="/Advisor", tags=["Advisor"])
api_router.include_router(user.router, prefix="/User", tags=["User"])
api_router.include_router(bucket.router, prefix="/Bucket", tags=["Bucket"])
api_router.include_router(
    bank_account_type.router, prefix="/BankAccountType", tags=["BankAccountType"]
)

api_router.include_router(event_type.router, prefix="/EventType", tags=["EventType"])
api_router.include_router(
    funds_category.router, prefix="/FundsCategory", tags=["FundsCategory"]
)
api_router.include_router(funds_type.router, prefix="/FundsType", tags=["FundsType"])
api_router.include_router(loan_type.router, prefix="/LoanType", tags=["LoanType"])
api_router.include_router(
    instrument_type.router, prefix="/InstrumentType", tags=["InstrumentType"]
)
api_router.include_router(
    relation_type.router, prefix="/RelationType", tags=["RelationType"]
)
api_router.include_router(
    retirement_status.router, prefix="/RetirementStatus", tags=["RetirementStatus"]
)
api_router.include_router(
    corpus_status.router, prefix="/CorpusStatus", tags=["CorpusStatus"]
)
api_router.include_router(
    portfolio_morning_star.router,
    prefix="/PortfolioMorningStar",
    tags=["PortfolioMorningStar"],
)
api_router.include_router(
    portfolio_morning_star.router,
    prefix="/PortfolioMorningStar",
    tags=["PortfolioMorningStar"],
)
api_router.include_router(
    areas_of_concerns.router, prefix="/AreasOfConcerns", tags=["AreasOfConcerns"]
)
api_router.include_router(
    asset_liability_category.router,
    prefix="/AssetLiabilityCategory",
    tags=["AssetLiabilityCategory"],
)
api_router.include_router(asset_type.router, prefix="/AssetType", tags=["AssetType"])
api_router.include_router(
    asset_allocation_attributes.router,
    prefix="/AssetAllocationAttributes",
    tags=["AssetAllocationAttributes"],
)
api_router.include_router(
    policy_weightage.router, prefix="/PolicyWeightage", tags=["PolicyWeightage"]
)
api_router.include_router(
    investment_type.router, prefix="/InvestmentType", tags=["InvestmentType"]
)
api_router.include_router(
    investment_bucket.router, prefix="/InvestmentBucket", tags=["InvestmentBucket"]
)
api_router.include_router(
    payment_type.router, prefix="/PaymentType", tags=["PaymentType"]
)
api_router.include_router(
    investment_vehicle.router, prefix="/InvestmentVehicle", tags=["InvestmentVehicle"]
)
api_router.include_router(
    investment_profile.router, prefix="/InvestmentProfile", tags=["InvestmentProfile"]
)
api_router.include_router(role.router, prefix="/Role", tags=["Role"])
api_router.include_router(
    question_type.router, prefix="/QuestionType", tags=["QuestionType"]
)
api_router.include_router(question.router, prefix="/Question", tags=["Question"])
api_router.include_router(choice.router, prefix="/Choice", tags=["Choice"])
api_router.include_router(
    user_answers.router, prefix="/UserAnswers", tags=["UserAnswers"]
)
api_router.include_router(user_result.router, prefix="/UserResult", tags=["UserResult"])
api_router.include_router(rate.router, prefix="/Rate", tags=["Rate"])
api_router.include_router(frequency.router, prefix="/Frequency", tags=["Frequency"])
api_router.include_router(goal_type.router, prefix="/GoalType", tags=["GoalType"])
api_router.include_router(
    other_goal_type.router, prefix="/OtherGoalType", tags=["OtherGoalType"]
)
api_router.include_router(income_type.router, prefix="/IncomeType", tags=["IncomeType"])
api_router.include_router(
    expense_type.router, prefix="/ExpenseType", tags=["ExpenseType"]
)
api_router.include_router(goal_bucket.router, prefix="/GoalBucket", tags=["GoalBucket"])
api_router.include_router(
    goal_category.router, prefix="/GoalCategory", tags=["GoalCategory"]
)
api_router.include_router(
    expense_category.router, prefix="/ExpenseCategory", tags=["ExpenseCategory"]
)
api_router.include_router(
    income_category.router, prefix="/IncomeCategory", tags=["IncomeCategory"]
)
api_router.include_router(user_goals.router, prefix="/UserGoals", tags=["UserGoals"])
api_router.include_router(
    user_incomes.router, prefix="/UserIncomes", tags=["UserIncomes"]
)
api_router.include_router(
    generated_buckets.router, prefix="/GeneratedBuckets", tags=["GeneratedBuckets"]
)
api_router.include_router(
    generated_goals.router, prefix="/GeneratedGoals", tags=["GeneratedGoals"]
)
api_router.include_router(
    generated_incomes.router, prefix="/GeneratedIncomes", tags=["GeneratedIncomes"]
)
api_router.include_router(
    generated_cash_ladder.router,
    prefix="/GeneratedCashLadder",
    tags=["GeneratedCashLadder"],
)
api_router.include_router(
    submit_question.router, prefix="/SubmitQuestion", tags=["SubmitQuestion"]
)
api_router.include_router(
    target_assets.router, prefix="/TargetAssets", tags=["TargetAssets"]
)
api_router.include_router(post_goal.router, prefix="/PostGoal", tags=["PostGoal"])
api_router.include_router(income.router, prefix="/Income", tags=["Income"])
api_router.include_router(
    submit_question.router, prefix="/SubmitQuestion", tags=["SubmitQuestion"]
)
api_router.include_router(kyc.router, prefix="/Kyc", tags=["Kyc"])
api_router.include_router(order.router, prefix="/Order", tags=["order"])
api_router.include_router(payment.router, prefix="/Payment", tags=["payment"])
api_router.include_router(
    bse_client_tax_status.router,
    prefix="/BseClientTaxStatus",
    tags=["BseClientTaxStatus"],
)
api_router.include_router(
    bse_account_type.router, prefix="/BseAccountType", tags=["BseAccountType"]
)
api_router.include_router(
    bse_client_occupation_code.router,
    prefix="/BseClientOccupationCode",
    tags=["BseClientOccupationCode"],
)
api_router.include_router(
    bse_communication_mode.router,
    prefix="/BseCommunicationMode",
    tags=["BseCommunicationMode"],
)
api_router.include_router(
    bse_pan_exempt_category.router,
    prefix="/BsePanExemptCategory",
    tags=["BsePanExemptCategory"],
)
api_router.include_router(
    bse_state_code.router, prefix="/BseStateCode", tags=["BseStateCode"]
)
api_router.include_router(
    bse_country_code.router, prefix="/BseCountryCode", tags=["BseCountryCode"]
)
api_router.include_router(
    nominee_relation.router, prefix="/NomineeRelation", tags=["NomineeRelation"]
)
api_router.include_router(
    bse_income_slab.router, prefix="/BSEIncomeSlab", tags=["BSEIncomeSlab"]
)
api_router.include_router(
    occupation_types.router, prefix="/OccupationTypes", tags=["OccupationTypes"]
)
api_router.include_router(
    source_of_wealth.router, prefix="/SourceOfWealth", tags=["SourceOfWealth"]
)
api_router.include_router(
    bse_client_code.router, prefix="/BseClientCode", tags=["BseClientCode"]
)
api_router.include_router(
    bse_client_nominee.router, prefix="/BseClientNominee", tags=["BseClientNominee"]
)
api_router.include_router(banks.router, prefix="/Banks", tags=["Banks"])
api_router.include_router(
    bank_branches.router, prefix="/BankBranches", tags=["BankBranches"]
)
api_router.include_router(sign_zy.router, prefix="/SignZy", tags=["SignZy"])
api_router.include_router(
    signzy_account.router, prefix="/SignzyAccount", tags=["SignzyAccount"]
)
api_router.include_router(
    bse_client_account.router, prefix="/BseClientAccount", tags=["BseClientAccount"]
)
api_router.include_router(refund.router, prefix="/Refund", tags=["Refund"])
api_router.include_router(refund.router, prefix="/Refund", tags=["Refund"])
api_router.include_router(settlement.router, prefix="/Settlement", tags=["Settlement"])
api_router.include_router(
    sustainability_score_configuration.router,
    prefix="/SustainabilityScoreConfiguration",
    tags=["SustainabilityScoreConfiguration"],
)
api_router.include_router(
    rr_score_configuration.router,
    prefix="/RrScoreConfiguration",
    tags=["RrScoreConfiguration"],
)
api_router.include_router(
    ability_configuration.router,
    prefix="/AbilityConfiguration",
    tags=["AbilityConfiguration"],
)
api_router.include_router(
    willingness_configuration.router,
    prefix="/WillingnessConfiguration",
    tags=["WillingnessConfiguration"],
)
api_router.include_router(
    risk_profile_configuration.router,
    prefix="/RiskProfileConfiguration",
    tags=["RiskProfileConfiguration"],
)
api_router.include_router(
    post_retirement_configuration.router,
    prefix="/PostRetirementConfiguration",
    tags=["PostRetirementConfiguration"],
)
api_router.include_router(
    pre_retirement_configuration.router,
    prefix="/PreRetirementConfiguration",
    tags=["PreRetirementConfiguration"],
)
api_router.include_router(
    cash_free_configuration.router,
    prefix="/CashFreeConfiguration",
    tags=["CashFreeConfiguration"],
)
api_router.include_router(
    pre_retirement_corpus_calculation.router,
    prefix="/PreRetirementCorpusCalculation",
    tags=["PreRetirementCorpusCalculation"],
)
api_router.include_router(
    pre_retirement_corpus_calculation.router,
    prefix="/PreRetirementCorpusCalculation",
    tags=["PreRetirementCorpusCalculation"],
)
api_router.include_router(
    pre_retirement_corpus_calculation.router,
    prefix="/PreRetirementCorpusCalculation",
    tags=["PreRetirementCorpusCalculation"],
)
api_router.include_router(user_assets.router, prefix="/UserAssets", tags=["UserAssets"])
api_router.include_router(
    users_re_balance_sheet.router,
    prefix="/UsersReBalanceSheet",
    tags=["UsersReBalanceSheet"],
)
api_router.include_router(
    daily_asset_data.router, prefix="/DailyAssetData", tags=["DailyAssetData"]
)
api_router.include_router(
    morning_star_navs.router, prefix="/MorningStarNavs", tags=["MorningStarNavs"]
)
api_router.include_router(
    daily_nav_data.router, prefix="/DailyNavData", tags=["DailyNavData"]
)
api_router.include_router(
    morning_star_navs.router, prefix="/MorningStarNavs", tags=["MorningStarNavs"]
)
api_router.include_router(
    assets_limit.router, prefix="/AssetsLimit", tags=["AssetsLimit"]
)
api_router.include_router(re_balance.router, prefix="/ReBalance", tags=["ReBalance"])
api_router.include_router(
    fund_level_asset_percent.router,
    prefix="/FundLevelAssetPercent",
    tags=["FundLevelAssetPercent"],
)
api_router.include_router(phone_api.router, prefix="/PhoneApi", tags=["PhoneApi"])
api_router.include_router(sustainability_score.router, prefix="/SustainabilityScore", tags=["SustainabilityScore"])
api_router.include_router(net_worth_bank_deposit_data.router, prefix="/NetWorthBankDepositData",
                          tags=["NetWorthBankDepositData"])
api_router.include_router(net_worth_fixed_deposit_data.router, prefix="/NetWorthFixedDepositData",
                          tags=["NetWorthFixedDepositData"])
api_router.include_router(net_worth_investment_data.router, prefix="/NetWorthInvestmentData",
                          tags=["NetWorthInvestmentData"])
api_router.include_router(net_worth_life_insurance_data.router, prefix="/NetWorthLifeInsuranceData",
                          tags=["NetWorthLifeInsuranceData"])
api_router.include_router(net_worth_other_asset_data.router, prefix="/NetWorthOtherAssetData",
                          tags=["NetWorthOtherAssetData"])
api_router.include_router(net_worth_house_data.router, prefix="/NetWorthHouseData", tags=["NetWorthHouseData"])
api_router.include_router(net_worth_vehicle_data.router, prefix="/NetWorthVehicleData", tags=["NetWorthVehicleData"])
api_router.include_router(net_worth_gold_data.router, prefix="/NetWorthGoldData", tags=["NetWorthGoldData"])
api_router.include_router(net_worth_others_data.router, prefix="/NetWorthOthersData", tags=["NetWorthOthersData"])
api_router.include_router(net_worth_stocks_data.router, prefix="/NetWorthStocksData", tags=["NetWorthStocksData"])
api_router.include_router(net_worth_others_data.router, prefix="/NetWorthOthersData", tags=["NetWorthOthersData"])
api_router.include_router(rr_score_result.router, prefix="/RrScoreResult", tags=["RrScoreResult"])
api_router.include_router(net_worth_bank_deposit_data.router, prefix="/NetWorthBankDepositData",
                          tags=["NetWorthBankDepositData"])
api_router.include_router(net_worth_fixed_deposit_data.router, prefix="/NetWorthFixedDepositData",
                          tags=["NetWorthFixedDepositData"])
api_router.include_router(net_worth_investment_data.router, prefix="/NetWorthInvestmentData",
                          tags=["NetWorthInvestmentData"])
api_router.include_router(net_worth_life_insurance_data.router, prefix="/NetWorthLifeInsuranceData",
                          tags=["NetWorthLifeInsuranceData"])
api_router.include_router(net_worth_other_asset_data.router, prefix="/NetWorthOtherAssetData",
                          tags=["NetWorthOtherAssetData"])
api_router.include_router(net_worth_category_data.router, prefix="/NetWorthCategoryData", tags=["NetWorthCategoryData"])
api_router.include_router(net_worth_bucket_data.router, prefix="/NetWorthBucketData", tags=["NetWorthBucketData"])
api_router.include_router(net_worth_loan_type_data.router, prefix="/NetWorthLoanTypeData",
                          tags=["NetWorthLoanTypeData"])
api_router.include_router(net_worth_scheme_type_data.router, prefix="/NetWorthSchemeTypeData",
                          tags=["NetWorthSchemeTypeData"])
api_router.include_router(net_worth_vehicle_type_data.router, prefix="/NetWorthVehicleTypeData",
                          tags=["NetWorthVehicleTypeData"])
api_router.include_router(net_worth_frequency_type_data.router, prefix="/NetWorthFrequencyTypeData",
                          tags=["NetWorthFrequencyTypeData"])
api_router.include_router(net_worth_user_table_data.router, prefix="/NetWorthUserTableData",
                          tags=["NetWorthUserTableData"])
api_router.include_router(marital_status.router, prefix="/MaritalStatus", tags=["MaritalStatus"])
api_router.include_router(rule_condition.router, prefix="/RuleCondition", tags=["RuleCondition"])
api_router.include_router(net_worth_calculation.router, prefix="/NetWorthCalculation", tags=["NetWorthCalculation"])
api_router.include_router(epf_calculation.router, prefix="/EpfCalculation", tags=["EpfCalculation"])
api_router.include_router(nps_calculation.router, prefix="/NpsCalculation", tags=["NpsCalculation"])
api_router.include_router(ppf_calculation.router, prefix="/PpfCalculation", tags=["PpfCalculation"])
api_router.include_router(bonds_calculation.router, prefix="/BondsCalculation", tags=["BondsCalculation"])
api_router.include_router(mf_calculation.router, prefix="/MfCalculation", tags=["MfCalculation"])
api_router.include_router(stocks_calculation.router, prefix="/StocksCalculation", tags=["StocksCalculation"])
api_router.include_router(others_calculation.router, prefix="/OthersCalculation", tags=["OthersCalculation"])
api_router.include_router(financial_amount_calculation.router, prefix="/FinancialAmountCalculation",
                          tags=["FinancialAmountCalculation"])

api_router.include_router(rule_asset_allocation.router, prefix="/RuleAssetAllocation", tags=["RuleAssetAllocation"])
api_router.include_router(asset_class_hierarchy.router, prefix="/AssetClassHierarchy", tags=["AssetClassHierarchy"])
api_router.include_router(asset_advisory.router, prefix="/AssetAdvisory", tags=["AssetAdvisory"])
api_router.include_router(cas_data_upload_to_pulse_lab.router, prefix="/CasDataUploadToPulseLab",
                          tags=["CasDataUploadToPulseLab"])
api_router.include_router(cas_data_upload_from_pulse_lab.router, prefix="/CasDataUploadFromPulseLab",
                          tags=["CasDataUploadFromPulseLab"])

api_router.include_router(epfo_auto_fetch.router, prefix="/EpfoAutoFetch", tags=["EpfoAutoFetch"])
api_router.include_router(cas_upload.router, prefix="/CasUpload", tags=["CasUpload"])