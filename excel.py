from pandas import DataFrame
def add_to_excel(ws_active: str, dataframe: DataFrame, column_df: str, column_excel: str,
                 row_offset: int = 0, column_offset: int = 2) -> None:
    """

    :param ws_active:
    :param dataframe:
    :param row_offset:
    :param column_offset:
    :param column_df:
    :param column_excel:
    :return None:
    """

    for category, value in dataframe.iterrows():
        # print(category)
        for cell in ws_active[column_excel]:
            tag = cell.value
            placement = cell.offset(row=row_offset, column=column_offset).coordinate
            print(tag)
            if tag is None:
                break

            # Убираем числа в начале строки
            if tag[0].isdigit():
                tag = tag[3:]

            if category.strip() == tag.strip():
                print(category, tag, value)
                ws_active[placement] = value[column_df]
                break

    return None
