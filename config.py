import os
from time import time
from utils import get_now_month_date
from dotenv import load_dotenv

load_dotenv(dotenv_path=r'D:\Pythonfail\My_Project\budget_lamer\.env')

# You can change it manually, in case some month is missed
now_month = get_now_month_date()[0]
active_list = get_now_month_date()[1]

# Parameters for the request to DzenMoney
url_api_dzen = r'https://api.zenmoney.ru/v8/diff/'
headers_api_dzen = {"Authorization": "Bearer {}".format(os.getenv("TOKEN_DZEN_MONEY"))}
params_api_dzen = {"currentClientTimestamp": time(), "serverTimestamp": 0}

# Parameters to request in MOEX
url_api_moex = r'https://iss.moex.com/iss/securities/ticker/aggregates.json'

# Excel Workbook Settings
path_placement_wb = r'D:\Pythonfail\My_Project\budget_lamer\budget\Budget.xlsx'
path_save_wb = r'D:\Pythonfail\My_Project\budget_lamer\budget\Budget.xlsx'
