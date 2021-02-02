import datetime

days = ["Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"]

d, m = map(int, input().split())

weekdays = datetime.date(2009,m,d).weekday()

print(days[weekdays])
