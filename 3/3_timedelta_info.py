from datetime import timedelta, datetime

"""
The datetime module has a timedelta class that is used to represent the difference between two points in time.
Object can be created with params days, seconds, microseconds, milliseconds, minutes, hours, weeks
if param is not set it will be equal to 0
if you deduct 1 datetime object from another you will receive timedelta obj
The maximum range for timedelta is limited to approximately 9999 years
"""

delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)

print (delta)


seventh_day_2019 = datetime(year=2019, month=1, day=1, hour=14)
seventh_day_2025 = datetime(year=2025, month=1,day=1, hour=20)

difference = seventh_day_2019 - seventh_day_2025
print(difference)
print(difference.total_seconds())

now = datetime.now()
future_date = now + timedelta(days=10) 
print(future_date)


"""We can use the toordinal() method, which returns the ordinal number of the day, given the number of days since January 1, 1 AD (i.e., the start of the Christian calendar). This method converts a datetime object to an integer representing the ordinal number of the given day."""
# Set the date of the burning of Moscow by Napoleon (September 14, 1812)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Current date
current_date = datetime.now()

# Calculate the number of days
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since)


""""
☝ timestamp is a universal way to represent time because it is independent of time zones and calendar systems.
"""

# Current time
now = datetime.now()

# Convert datetime to timestamp
timestamp = datetime.timestamp(now)
print(timestamp) # Print the timestamp of the current time


from datetime import datetime


timestamp = 1617183600

#  timestamp to datetime
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)  
