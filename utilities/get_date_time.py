from datetime import date


def get_next_month_func():
    today_date = date.today()
    year = today_date.year
    month = today_date.month

    if month == 12:
        return f"{year + 1}-01"
    elif month >= 9:
        return f"{year}-{month + 1}"
    else:
        return f"{year}-0{month + 1}"


def get_previous_month_func():
    today_date = date.today()
    year = today_date.year
    month = today_date.month

    if month == 1:
        return f"{year - 1}-12"
    elif month <= 10:
        return f"{year}-0{month - 1}"
    else:
        return f"{year}-{month - 1}"


def get_previous_day_func():
    today_date = date.today()
    year = today_date.year
    month = today_date.month

    if month > 9:
        return f"{year}-{month}-{today_date.day - 1}"
    else:
        return f"{year}-0{month}-{today_date.day - 1}"


def get_current_day_func():
    today_date = date.today()
    year = today_date.year
    month = today_date.month

    if int(month) > 9:
        return f"{year}-{month}-{today_date.day}"
    else:
        return f"{year}-0{month}-{today_date.day}"


