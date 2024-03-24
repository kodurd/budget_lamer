import pandas as pd
from utils import transform_in_dict, drop_trash_string
from openpyxl.worksheet import worksheet


def get_place_on_col(ws: worksheet.Worksheet, columns: list) -> pd.DataFrame:
    """Читаем значение по столбцу или по нескольким или же по заданному диапозону"""

    placements = [transform_in_dict([drop_trash_string(cell.value), cell.coordinate])
                  for column in columns
                  for cell in ws[column] if cell.value is not None]

    return pd.DataFrame(placements)


def get_place_on_range(ws: worksheet.Worksheet, span: list) -> pd.DataFrame:
    """Читаем значение по диапозону"""

    placements = [transform_in_dict([drop_trash_string(cell.value), cell.coordinate])
                  for cell_object in ws[span[0]:span[1]]
                  for cell in cell_object if cell.value is not None]

    return pd.DataFrame(placements)


def add_to_excel(ws: worksheet.Worksheet, data_budget: pd.DataFrame, data_cells: pd.DataFrame,
                 col_offset: int = 1, row_offset: int = 0) -> None:
    """Заполнение книги Excel сравнивая строки"""

    for name, value in data_budget.iterrows():
        try:
            cell = data_cells.loc[data_cells['value'] == name]['placement'].iloc[0]
        except Exception:
            raise Exception(f"На листе Excel отсутствует данная категория: {name}")

        ws[cell].offset(row=row_offset, column=col_offset).value = value.iloc[0]
