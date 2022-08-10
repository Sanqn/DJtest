import datetime
import calendar

days = []
now = datetime.datetime.now()
year = now.year
month = 1


def calend_mounth():

    global days
    info_label = calendar.day_name[2] + ', ' + calendar.month_name[month] + ', ' + str(year)
    print(info_label)
    month_days = calendar.monthrange(year, month)[1]
    print('month_days ', month_days)
    if month == 1:
        prew_month_days = calendar.monthrange(year - 1, 12)[1]
    else:
        prew_month_days = calendar.monthrange(year, month - 1)[1]
        print('prew_month_days ', prew_month_days)

    week_day = calendar.monthrange(year, month)[0]
    print('week_day ', week_day)
    for n in range(month_days):
        days.append(n + 1)
    for n in range(week_day + 1):
        days = [prew_month_days - n] + days

    for n in range(6 * 7 - month_days - week_day - 1):
        days.append(n + 1)
    print(days)
    print(len(days))


calend_mounth()
