"""
provide classes for work with dates and time

datetime.now(): This method returns a datetime object that contains the current date and time.

datetime.date(): This method returns a date object that represents only the date (without the time).

datetime.time(): The method returns a time object that contains only the time (no date).

datetime.combine(date, time): This method is used to combine date and time objects and create a new datetime object.

datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0): The constructor of the datetime class allows you to create a datetime object with a specific date and time.

weekday(): The method determines the number of the day of the week for the specified date, where Monday is number 0 and Sunday is number 6.
"""
from datetime import datetime, date, time

current_datetime = datetime.now()  # Now this works correctly

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo)
print(current_datetime.date())
print(current_datetime.time())

date_part = date(2023, 12, 14)
print(date_part)
time_part = time(12, 30, 15)
print(time_part)
print(datetime.combine(date_part, time_part))

# Using key parameters makes the code more understandable, especially when read by other developers.
specific_datetime = datetime(
    year=2025, month=3, day=18
)  
print(specific_datetime)

now = datetime.now()
day_of_week = now.weekday()


print(f'Today is: {day_of_week}')

datetime1 = datetime(2025, 3, 3)
datetime2 = datetime(2025, 3, 18)

# we can compare dates using regular mathematical expressions
print( datetime1 < datetime2)
