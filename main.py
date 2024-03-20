import datetime

from utils import connect_api, add_to_excel
from time import time
import json
from dotenv import load_dotenv
import os
import pandas as pd
from openpyxl import load_workbook

pd.set_option('display.max_columns', 1000)
load_dotenv(dotenv_path=r'D:\Pythonfail\My_Project\budget_lamer\.env')

token = os.getenv("TOKEN_DZEN_MONEY")
now_month = datetime.date.today().strftime('%Y-%m')
param = {"currentClientTimestamp": time(), "serverTimestamp": 0}
headers = {"Authorization": "Bearer {}".format(token)}


dataset = connect_api(url=r'https://api.zenmoney.ru/v8/diff/',
                      method='POST',
                      headers=headers,
                      json=param).json()






wb = load_workbook(filename=r'D:\Pythonfail\My_Project\budget_lamer\Budget_2024.xlsx')
ws = wb['April']

add_to_excel(ws_active=ws, dataframe=df_budget, column_df='outcome', column_excel='A')
# Добавление доходов
pass

wb.save('XXX.xlsx')



