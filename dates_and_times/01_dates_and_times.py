from datetime import date, time, datetime

d1 = date.today()
print(d1, d1.year, d1.month, d1.day, d1.weekday())

t1 = time(12, 30)
print(t1, t1.hour, t1.minute)

dt1 = datetime.now()
print(dt1.month, dt1.weekday())


def current_day():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    return days[datetime.now().weekday()]


print(current_day())


d1 = d1.replace(year=2020, month=1, day=1)
print(d1)

t1 = t1.replace(hour=9)
print(t1)

dt1 = dt1.replace(year=2000)
print(dt1)
