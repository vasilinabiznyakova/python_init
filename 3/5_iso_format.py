"""
The ISO 8601:
- date format looks like "YYYY-MM-DD"
- time format in ISO 8601 looks like "HH:MM:SS"

"YYYY-MM-DDTHH:MM:SS"
"""
from datetime import datetime, timezone, timedelta


# Current date and time
now = datetime.now()
# Convert to ISO 8601 format
iso_format = now.isoformat()
print(iso_format)



iso_date_string = "2023-03-14T12:39:29.992996"

# Конвертація з ISO формату
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso)



# Create a datetime object
now = datetime.now()

# Use isoweekday() to get the day of the week
day_of_week = now.isoweekday()

print(f"Today is: {day_of_week}") # Returns a number from 1 to 7 that corresponds to the day of the week


"""The isocalendar() method is useful in situations where you need to work with weekly intervals or calculate dates in a format widely used in business planning and logistics. It can also be useful for determining a specific week of the year for events or when scheduling tasks."""

# Create a datetime object
now = datetime.now()

# Get the ISO calendar
iso_calendar = now.isocalendar()

print(f"ISO year: {iso_calendar[0]}, ISO week: {iso_calendar[1]}, ISO day of the week: {iso_calendar[2]}")


local_now = datetime.now()
utc_now = datetime.now(timezone.utc)

print(local_now)
print(utc_now)  # current time in UTC


utc_time = datetime.now(timezone.utc)

# Create a time zone for Eastern Time Zone (UTC-5)

eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Converts UTC time to Eastern Time Zone time
print(eastern_time)