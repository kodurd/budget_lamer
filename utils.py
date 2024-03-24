from datetime import date


def drop_trash_string(string: str, right_offset: int = 2) -> str:
    """Удаляем мусор из строки, смещая ее по заданному параметру"""
    if string[0].isdigit():
        string = string[right_offset:].strip()
    return string


def transform_in_dict(values: list) -> dict:
    """Преобразовывает только два значения в словарь"""
    if len(values) != 2:
        raise ValueError("Список должен содержать только два аргумента")

    return {'value': values[0], 'placement': values[1]}


def get_now_month_date():
    """Получаем текущий месяц в формате '%Y-%m' и в формате текста (%B)"""
    now_month_date = date.today().strftime('%Y-%m')
    now_mont_text = date.today().strftime('%B')
    return now_month_date, now_mont_text
