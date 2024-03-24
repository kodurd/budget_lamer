import datetime
from connect import connect_api
from processing import processing_budget
from time import time
from dotenv import load_dotenv
import os
import pandas as pd
from openpyxl import load_workbook


# Отключаем предупреждения openpyxl

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

df_budget, df_account = processing_budget(dataset, now_month)






add_to_excel(ws=ws, data_budget=df_budget, data_cells=data_cells, col_offset=2)


# Получить тикеры
# range = ['G32', 'G34']
# df_ticer = pd.DataFrame(get_place_on_range(ws, range))
#
# print(df_ticer)
#
# data = connect_api()


wb.save('XXX.xlsx')
