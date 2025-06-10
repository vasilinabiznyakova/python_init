from datetime import date, MINYEAR, MAXYEAR

today = "11.06.2025"

d = date.today()
print(d.day)  # property
print(d.month)
print(d.year)


created_date = date(year=2013, day=1, month=5)
print(created_date)
print(MINYEAR)
print(MAXYEAR)


created_date = date(year=2013, day=25, month=1)


import calendar

terminal_calendar = calendar.calendar(2025)
print(terminal_calendar)


from datetime import datetime

d = datetime.now()
print(d.second)
d = datetime(2025, 5, 3)
print(d)


# strptime string parse time

# strptime string format time


