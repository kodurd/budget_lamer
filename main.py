import datetime
from connect import connect_api
from excel import add_to_excel
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
# print(df_account[['title', 'balance']])

# Добавление расходов
# add_to_excel(ws_active=ws, dataframe=df_budget, column_df='outcome', column_excel='A')
# # Добавление доходов
# add_to_excel(ws_active=ws, dataframe=df_budget, column_df='income', column_excel='G')
# Добавление баланса счетов
add_to_excel(ws_active=ws, dataframe=df_account[['title', 'balance']].set_index('title'),
             column_df='balance', column_excel='G', column_offset=1)

# for i, x in df_account[['title', 'balance']].set_index('title').iterrows():
#     print(x['balance'])

# for i, x in df_budget.iterrows():
#     print(x)

wb.save('XXX.xlsx')
