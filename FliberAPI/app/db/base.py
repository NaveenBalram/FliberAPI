# Import all the models, so that Base has them before being imported by Alembic

from app.db.base_class import Base
from app.db.tables.gender import Gender
from app.db.tables.advisor import Advisor
from app.db.tables.user import User
from app.db.tables.bucket import Bucket
from app.db.tables.generated_buckets import GeneratedBuckets
from app.db.tables.generated_goals import GeneratedGoals
from app.db.tables.generated_incomes import GeneratedIncomes
from app.db.tables.generated_cash_ladder import GeneratedCashLadder
from app.db.tables.bank_account_type import BankAccountType
from app.db.tables.marital_status import MaritalStatus
from app.db.tables.event_type import EventType
from app.db.tables.funds_category import FundsCategory
from app.db.tables.funds_type import FundsType
from app.db.tables.loan_type import LoanType
from app.db.tables.instrument_type import InstrumentType
from app.db.tables.relation_type import RelationType
from app.db.tables.retirement_status import RetirementStatus
from app.db.tables.corpus_status import CorpusStatus
from app.db.tables.portfolio_morning_star import PortfolioMorningStar
from app.db.tables.areas_of_concerns import AreasOfConcerns
from app.db.tables.asset_liability_category import AssetLiabilityCategory
from app.db.tables.asset_type import AssetType
from app.db.tables.asset_allocation_attributes import AssetAllocationAttributes
from app.db.tables.policy_weightage import PolicyWeightage
from app.db.tables.investment_type import InvestmentType
from app.db.tables.investment_bucket import InvestmentBucket
from app.db.tables.payment_type import PaymentType
from app.db.tables.investment_vehicle import InvestmentVehicle
from app.db.tables.investment_profile import InvestmentProfile
from app.db.tables.role import Role
from app.db.tables.question_type import QuestionType
from app.db.tables.question import Question
from app.db.tables.choice import Choice
from app.db.tables.submit_question import SubmitQuestion
from app.db.tables.target_assets import TargetAssets
from app.db.tables.user_answers import UserAnswers
from app.db.tables.user_result import UserResult
from app.db.tables.rate import Rate
from app.db.tables.frequency import Frequency
from app.db.tables.goal_type import GoalType
from app.db.tables.other_goal_type import OtherGoalType
from app.db.tables.income_type import IncomeType
from app.db.tables.expense_type import ExpenseType
from app.db.tables.goal_bucket import GoalBucket
from app.db.tables.goal_category import GoalCategory
from app.db.tables.expense_category import ExpenseCategory
from app.db.tables.income_category import IncomeCategory
from app.db.tables.user_goals import UserGoals
from app.db.tables.user_incomes import UserIncomes
from app.db.tables.post_goal import PostGoal
from app.db.tables.income import Income
from app.db.tables.user_info import UserInfo
from app.db.tables.generated_cash_ladder_pre import GeneratedCashLadderPre
from app.db.tables.kyc import Kyc
from app.db.tables.order import Order
from app.db.tables.payment import Payment
from app.db.tables.bse_client_holding import BseClientHolding
from app.db.tables.bse_client_tax_status import BseClientTaxStatus
from app.db.tables.bse_account_type import BseAccountType
from app.db.tables.bse_client_occupation_code import BseClientOccupationCode
from app.db.tables.bse_communication_mode import BseCommunicationMode
from app.db.tables.bse_pan_exempt_category import BsePanExemptCategory
from app.db.tables.bse_state_code import BseStateCode
from app.db.tables.bse_country_code import BseCountryCode
from app.db.tables.nominee_relation import NomineeRelation
from app.db.tables.bse_income_slab import BSEIncomeSlab
from app.db.tables.occupation_types import OccupationTypes
from app.db.tables.source_of_wealth import SourceOfWealth
from app.db.tables.bse_client_code import BseClientCode
from app.db.tables.bse_client_nominee import BseClientNominee
from app.db.tables.banks import Banks
from app.db.tables.bank_branches import BankBranches
from app.db.tables.sign_zy import SignZy
from app.db.tables.signzy_account import SignzyAccount
from app.db.tables.signzy_users import SignzyUsers
from app.db.tables.bse_client_account import BseClientAccount
from app.db.tables.refund import Refund
from app.db.tables.refund import Refund
from app.db.tables.settlement import Settlement
from app.db.tables.sustainability_score_configuration import (
    SustainabilityScoreConfiguration,
)
from app.db.tables.rr_score_configuration import RrScoreConfiguration
from app.db.tables.ability_configuration import AbilityConfiguration
from app.db.tables.willingness_configuration import WillingnessConfiguration
from app.db.tables.risk_profile_configuration import RiskProfileConfiguration
from app.db.tables.post_retirement_configuration import PostRetirementConfiguration
from app.db.tables.pre_retirement_configuration import PreRetirementConfiguration
from app.db.tables.cash_free_configuration import CashFreeConfiguration
from app.db.tables.pre_retirement_corpus_calculation import (
    PreRetirementCorpusCalculation,
)
from app.db.tables.morning_star_navs import MorningStarNavs
from app.db.tables.users_re_balance_sheet import UsersReBalanceSheet
from app.db.tables.user_assets import UserAssets
from app.db.tables.daily_asset_data import DailyAssetData
from app.db.tables.daily_nav_data import DailyNavData
from app.db.tables.assets_limit import AssetsLimit
from app.db.tables.fund_level_asset_percent import FundLevelAssetPercent
from app.db.tables.phone_api import PhoneApi
from app.db.tables.net_worth_fixed_deposit_data import NetWorthFixedDepositData
from app.db.tables.net_worth_bank_deposit_data import NetWorthBankDepositData
from app.db.tables.net_worth_investment_data import NetWorthInvestmentData
from app.db.tables.net_worth_other_asset_data import NetWorthOtherAssetData
from app.db.tables.net_worth_category_data import NetWorthCategoryData
from app.db.tables.net_worth_life_insurance_data import NetWorthLifeInsuranceData
from app.db.tables.net_worth_loan_type_data import NetWorthLoanTypeData
from app.db.tables.net_worth_user_table_data import NetWorthUserTableData
from app.db.tables.net_worth_vehicle_type_data import NetWorthVehicleTypeData
from app.db.tables.net_worth_bucket_data import NetWorthBucketData
from app.db.tables.net_worth_frequency_type_data import NetWorthFrequencyTypeData
from app.db.tables.net_worth_scheme_type_data import NetWorthSchemeTypeData
from app.db.tables.net_worth_annuity_data import NetWorthAnnuityData
from app.db.tables.net_worth_business_income_data import NetWorthBusinessIncomeData
from app.db.tables.net_worth_gold_data import NetWorthGoldData
from app.db.tables.net_worth_house_data import NetWorthHouseData
from app.db.tables.net_worth_loan_data import NetWorthLoanData
from app.db.tables.net_worth_other_income_data import NetWorthOtherIncomeData
from app.db.tables.net_worth_others_data import NetWorthOthersData
from app.db.tables.net_worth_rental_income_data import NetWorthRentalIncomeData
from app.db.tables.net_worth_stocks_data import NetWorthStocksData
from app.db.tables.net_worth_vehicle_data import NetWorthVehicleData
from app.db.tables.rule_condition import RuleCondition
from app.db.tables.rule_asset_allocation import RuleAssetAllocation
from app.db.tables.asset_class_hierarchy import AssetClassHierarchy
from app.db.tables.rr_score_result import RrScoreResult
from app.db.tables.universe_table import UniverseTable
from app.db.tables.cas_data_upload_from_pulse_lab import CasDataUploadFromPulseLab
from app.db.tables.financial_user_table import FinancialUserTable
from app.db.tables.financial_amount_calculation import FinancialAmountCalculation
