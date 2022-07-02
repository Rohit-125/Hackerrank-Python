import calendar
weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
m, d, y = map(int, input().split())
a = calendar.weekday(y, m, d)
print(weekdays[a])
