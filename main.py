import datetime

from getter import connect_api
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

df_transaction = pd.DataFrame(dataset.get('transaction', {}))
df_tag = pd.DataFrame(dataset.get('tag', {}))[['id', 'title']]
df_account = pd.DataFrame(dataset.get('account', {}))[['id', 'title', 'balance']]

# Фильтруем транзакции
df_transaction['date'] = df_transaction['date'].astype('datetime64[ns]')
df_transaction['year_month'] = df_transaction['date'].dt.to_period('M')
df_transaction = df_transaction.loc[(df_transaction['year_month'] == now_month) & (df_transaction['deleted'] == 0)]
df_transaction = df_transaction[['date', 'income', 'outcome', 'incomeAccount', 'outcomeAccount', 'tag']]
df_transaction['tag'] = df_transaction['tag'].map(lambda x: x[0] if x is not None else x)

# Объединим dataframes
df_transaction = (df_transaction.merge(df_tag, left_on='tag', right_on='id', how='left')
                                .merge(df_account, left_on='incomeAccount', right_on='id', how='left')
                                .merge(df_account, left_on='outcomeAccount', right_on='id', how='left'))
df_transaction.rename(columns={'title_x': 'category',
                               'title_y': 'income_account',
                               'title': 'outcome_account'}, inplace=True)
df_transaction = df_transaction[['date', 'income', 'outcome', 'income_account', 'outcome_account', 'category']]
# print(df_transaction)
#
# print(df_transaction.groupby(['category']).agg({'outcome': ['sum'],
#                                                 'income': ['sum']}))


# Другая функция
wb = load_workbook(filename=r'D:\Pythonfail\My_Project\budget_lamer\Budget_2024.xlsx')
ws = wb['April']['A']

# Сначала ищем значение в истинных расходах, потом находим в книге, ну и прибаляем +2
for i in range(len(ws)):
    print(ws[i].value)