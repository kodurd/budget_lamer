from config import *
from excel import *
from utils import get_now_month_date
from connect import connect_api
from processing import processing_budget
import pandas as pd
from openpyxl import load_workbook

# Отключаем предупреждения openpyxl
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 1000)


# Получаем сгрупированный по доходам и расходам датасет бюджета
dataset_budget = connect_api(url=url_api_dzen,
                             method='POST',
                             headers=headers_api_dzen,
                             json=params_api_dzen).json()
# Получаем датасет по котировкам
dataset_quotes = '...'
# Получаем датасет по валютам
dataset_currency = '...'


# Обрабатываем полученные датасеты (приводим к нужному виду)
df_budget, df_account = processing_budget(dataset=dataset_budget, now_month=get_now_month_date()[0])

df_outcome = df_budget[df_budget['outcome'] != 0][['outcome']]
df_income = df_budget[df_budget['income'] != 0][['income']]
df_account = df_account[df_account['balance'] != 0][['title', 'balance']].set_index('title')

# Открываем книгу для работы с ней
wb = load_workbook(filename=path_placement_wb)
ws = wb[active_list]

# Получаем месторасположение категорий и тикеров в книге Excel
placements_category_excel = get_place_on_col(ws=ws, columns=['A', 'G'])
placement_tickers = get_place_on_range(ws=ws, span=['G32', 'G34'])

# Заполняем книгу
add_to_excel(ws=ws, data_budget=df_outcome, data_cells=placements_category_excel, col_offset=2)
add_to_excel(ws=ws, data_budget=df_income, data_cells=placements_category_excel, col_offset=2)
add_to_excel(ws=ws, data_budget=df_account, data_cells=placements_category_excel, col_offset=1)

wb.save(filename=path_save_wb)


# Получить тикеры
pass


