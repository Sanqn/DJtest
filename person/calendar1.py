import datetime
import calendar


def calend_month(date):
    days = []
    a = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M')
    month = int(a.strftime("%m"))
    year = int(a.strftime("%Y"))
    info_label = calendar.day_name[2] + ', ' + calendar.month_name[month] + ', ' + str(year)
    print(info_label)
    month_days = calendar.monthrange(year, month)[1]
    if month == 1:
        prew_month_days = calendar.monthrange(year - 1, 12)[1]
    else:
        prew_month_days = calendar.monthrange(year, month - 1)[1]

    week_day = calendar.monthrange(year, month)[0]
    for n in range(month_days):
        days.append(str(year) + '-' + str(month) + '-' + str(n + 1))
    for n in range(week_day + 1):
        days = [str(year) + '-' + str(month - 1) + '-' + str(prew_month_days - n)] + days

    for n in range(6 * 7 - month_days - week_day - 1):
        days.append(str(year) + '-' + str(month + 1) + '-' + str(n + 1))
        # for i in days:
        #     print(datetime.datetime.strptime(i, '%Y-%m-%d'))
    new_days = [str(datetime.datetime.strptime(i, '%Y-%m-%d')).split(' ')[0] for i in days]
    return new_days
