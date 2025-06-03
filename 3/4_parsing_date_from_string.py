"""strftime method is used to format datetime objects into strings using specific format codes.

%Y - year with four digits (for example, 2023).
%y - year with two digits (for example, 23).
%m - month as a number (for example, 03 for March).
%d - day of the month as a number (for example, 14).
%H - hour (24-hour format) (for example, 15).
%I - hour (12-hour format) (for example, 03).
%M - minutes (e.g. 05).
%S - seconds (e.g. 09).
%A - full name of the day of the week (e.g. Tuesday).
%a - abbreviated name of the day of the week (e.g. Tue).
%B - full name of the month (e.g. March).
%b or %h - abbreviated name of the month (e.g. Mar).
%p - AM or PM for 12-hour format.
"""

from datetime import datetime
now = datetime.now()

print(now)

# Formatting date and time
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date) 

# Formatting date only
formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only)

# Formatting time only
formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only) 

# Formatting date only
formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only)


# strptime is used to create object datetime from string

date_string = "2023.03.14"
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)