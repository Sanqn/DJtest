import datetime
import calendar




def calend_mounth(date):
    days = []
    new_days = []
    j = []
    a = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M')
    month = int(a.strftime("%m"))
    year = int(a.strftime("%Y"))

    print(year, 'year ----------------------')
    print(month, 'month ----------------------')
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
        days.append(str(year) + '-' + str(month) + '-' + str(n + 1))
    for n in range(week_day + 1):
        days = [str(year) + '-' +str(month - 1) + '-' + str(prew_month_days - n)] + days

    for n in range(6 * 7 - month_days - week_day - 1):
        days.append(str(year) + '-' + str(month + 1) + '-' + str(n + 1))
    new_days = [str(datetime.datetime.strptime(i, '%Y-%m-%d')).split(' ')[0] for i in days]
    print(new_days)
    return j

print(calend_mounth('2022-08-04T12:40'))

# a = '9-8'
# print(datetime.datetime.strptime(a, "%d-%m"))

# request_time='2012-09-09'
# time_split=[int(x) for x in request_time.split('-')]
# times='%s-%s-%s'%(time_split[0],time_split[1],time_split[2]+1)
# cday = datetime.datetime.strptime(times, '%Y-%m-%d')
# print(cday, '====================')

# start_date = datetime.date(2009, 1, 1)
# print(start_date)
#
# a = 'Привет'
# print(a)
#
# b = '2022-08-24 00:00:00'
# c = '2022-08-24'
# if c in b:
#     print('ok')
# else:
#     print('Bed')