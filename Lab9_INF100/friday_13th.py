from datetime import datetime, timedelta


def first_friday_13th_after(date):
    if date.day == 13 and date.weekday() == 4:
        date += timedelta(days=1)
    while True:
        if date.day == 13 and date.weekday() == 4:
            return date
        date += timedelta(days=1)