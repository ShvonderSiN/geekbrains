from datetime import datetime

__all__ = ['check_date']



def _is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def check_date(date: str) -> bool:
    """Проверяет дату на корректность"""
    start = datetime(year=2, month=1, day=2)
    end = datetime(year=9999, month=12, day=31)
    try:
        date = datetime.strptime(date, '%d.%m.%Y')
        leap = 'високосный' if _is_leap_year(date.year) else 'не високосный'
        print(leap)
        # if start > date > end: #  почему-то такая конструкция не заработала
        if date < start or date > end:
            return False
        return True
    except ValueError:
        return False
