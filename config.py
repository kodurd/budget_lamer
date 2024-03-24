import os
from time import time
from utils import get_now_month_date
from dotenv import load_dotenv

load_dotenv(dotenv_path=r'D:\Pythonfail\My_Project\budget_lamer\.env')

# Параметры для запроса в DzenMoney
url_api_dzen = r'https://api.zenmoney.ru/v8/diff/'
headers_api_dzen = {"Authorization": "Bearer {}".format(os.getenv("TOKEN_DZEN_MONEY"))}
params_api_dzen = {"currentClientTimestamp": time(), "serverTimestamp": 0}

# Парметры для запроса в ALPHA_VANTAGE
pass

# Параметры книги excel
path_placement_wb = r'D:\Pythonfail\My_Project\budget_lamer\Budget_2024.xlsx'
path_save_wb = r'D:\Pythonfail\My_Project\budget_lamer\XXX.xlsx'
active_list = get_now_month_date()[1] # Можно менять в ручную, если что-то необходимо изменить
active_list = 'April'


