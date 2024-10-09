# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import sys

def _is_not_leap(year: int) -> bool:
    return not (year % 400 == 0 or year % 100 != 0 and year % 4 == 0)

def check_date(full_date: str) -> bool:
    day, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    elif month == 2 and day > 28 and _is_not_leap(year):
        return False
    else:
        return True

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Проверьте дату, она должна быть в виде DD.MM.YYYY")
        sys.exit(1)

    date_input = sys.argv[1]
    result = check_date(date_input)

    if result:
        print(f"Дата {date_input} существует.")
    else:
        print(f"Дата {date_input} не существует.")