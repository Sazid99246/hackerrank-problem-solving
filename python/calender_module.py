import calendar

month, day, year = map(int, input().split())
weekday_index = calendar.weekday(year, month, day)
weekday_name = calendar.day_name[weekday_index]

print(weekday_name.upper())
