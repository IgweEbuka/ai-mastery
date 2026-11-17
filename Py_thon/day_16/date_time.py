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
- The strptime() method creates a datetime object from the given string.
- Timedelta import can take week, days, hours and mins.
"""

from datetime import datetime, date, time, timedelta

# Formatting Date Output Using strftime

now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minutes = now.minute
second = now.second
timestamp = now.timestamp()

# print(f"Todays date is {day}/{month}/{year}. The time is {hour}:{minutes}:{second}. The timestamp is {timestamp}.")


# String to Time Using strptime

date_string = "18 December, 2026"
# print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
# print(date_object)


# Difference Between Two Points in Time Using

today = datetime(year=2026, month= 11, day= 16, hour=hour, minute= minutes, second= second)
new_year = datetime(year=2027, month=1, day=1)

new_year_in = new_year - today

# print(new_year_in)

# Exercises 

# 1

r_now = datetime.now()

day_1 = r_now.day
month_1 = r_now.month
year_1 = r_now.year

print(f'{day_1}--{month_1}--{year_1}')

# 2

drn = now.strftime("%d/%m/%Y, %H:%M:%S")
print(drn)

# 3

date_string_0 = "5 December, 2019"

date_new_object = datetime.strptime(date_string_0, "%d %B, %Y")
print(date_new_object)

# 4

today = datetime(year=2026, month= 11, day= 16, hour=hour, minute= minutes, second= second)
new_year = datetime(year=2027, month=1, day=1)

new_year_in = new_year - today
print(f"It will be a new year in {new_year_in}.")

# 5
then = datetime(year=1970, month=1, day=1)
time_slayer = today - then
print(f"1st January 1970 was {time_slayer} ago.")
