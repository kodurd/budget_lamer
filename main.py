from openpyxl import load_workbook
from config import *
from excel import *
from getter import *
from processing import *

# Disabling openpyxl warnings, as it does not support conditional formatting
import warnings
warnings.filterwarnings('ignore')

# Getting data from the DZEN MONEY API
dataset_budget = connect_api(url=url_api_dzen,
                             method='POST',
                             headers=headers_api_dzen,
                             json=params_api_dzen).json()

df_budget, df_account = groups_df_api_dzen(dataset=dataset_budget, now_month=now_month)

df_outcome = df_budget[df_budget['outcome'] != 0][['outcome']]
df_income = df_budget[df_budget['income'] != 0][['income']]

wb = load_workbook(filename=path_placement_wb)
ws = wb[active_list]

# We get the location of the expense and income categories and tickers in the Excel workbook
placements_category_excel = get_place_on_col(ws=ws, columns=['A', 'G'])
placement_tickers = get_place_on_range(ws=ws, span=['G32', 'G34'])

# Getting data from the MOEX API
dataset_quotes = get_data_moex(url=url_api_moex, tickers=placement_tickers['value'].to_list())
df_tickers = groups_df_api_moex(dataset=dataset_quotes)

# Filling out an Excel workbook
add_to_excel(ws=ws, df_write=df_outcome, df_excel=placements_category_excel, col_offset=2)
add_to_excel(ws=ws, df_write=df_income, df_excel=placements_category_excel, col_offset=2)
add_to_excel(ws=ws, df_write=df_account, df_excel=placements_category_excel, col_offset=1)
add_to_excel(ws=ws, df_write=df_tickers, df_excel=placement_tickers, col_offset=3)

wb.save(filename=path_save_wb)
