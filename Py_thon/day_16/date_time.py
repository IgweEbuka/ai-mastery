"""
- Python has got datetime module to handle date and time.
- From datetime import datetime.
- .strftime is used to format date and time.
- There are various symbols used to simplify this process:
    > %a - weekday, short.
    > %A - weekday, full.
    > %w - weekday,number(0-6, sunday is 0).
    > %d - day of the month(1-31).
    > %b - month name, short.
    > %B - month name, full.
    > %m - month number.
    > %y - year number, without century(26).
    > %Y - year number, full(2026).
    > %H - 24 hour clock display(00-23).
    > %I - 12 hour clock display(00-12).
    > %P - AM/PM etc.
- 
"""

from datetime import datetime

now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minutes = now.minute
second = now.second
timestamp = now.timestamp()

print(f"Todays date is {day}/{month}/{year}. The time is {hour}:{minutes}:{second}. The timestamp is {timestamp}.")

# Formatting Date Output Using strftime
