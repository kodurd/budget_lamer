from datetime import date
from typing import Tuple


def drop_trash_string(string: str, right_offset: int = 2) -> str:
    """Remove garbage from a row by shifting it by the specified parameter"""
    if string[0].isdigit():
        string = string[right_offset:].strip()
    return string


def transform_in_dict(values: list) -> dict:
    """Converts only two values into a dictionary of a certain structure:
    {value':values[0], 'placement': values[1]}
    """
    if len(values) != 2:
        raise ValueError("Список должен содержать только два аргумента")

    return {'value': values[0], 'placement': values[1]}


def get_now_month_date() -> Tuple[str, str]:
    """We get the current month in the format '%Y-%m' and in the text format %B"""
    now_month_date = date.today().strftime('%Y-%m')
    now_mont_text = date.today().strftime('%B')
    return now_month_date, now_mont_text
