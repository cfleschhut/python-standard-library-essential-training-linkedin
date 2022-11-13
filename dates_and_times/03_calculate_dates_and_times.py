import datetime

dt1 = datetime.datetime(2019, 1, 15, 10)
dt2 = datetime.datetime(2019, 1, 20, 15)

print(dt1 < dt2)
print(dt1 > dt2)

delta = dt2 - dt1
print(delta, delta.days, delta.seconds)


def one_year_from_now():
    return datetime.datetime.now() + datetime.timedelta(days=365)


def one_week_from_now():
    return datetime.datetime.now() + datetime.timedelta(weeks=1)


def one_week_ago():
    return datetime.datetime.now() + datetime.timedelta(weeks=-1)


print(one_year_from_now())
print(one_week_from_now())
print(one_week_ago())
