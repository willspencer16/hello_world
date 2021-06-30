# Working with timedelta objects:

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# Constructing a basic timedelta:
print(timedelta(days=365, hours=5, minutes=1))

# Printing today's date
now = datetime.now()
print("Today is: " + str(now))

# Printing today's date one year from now:
print("One year from now it will be: " + str(now + timedelta(days=365)))

# Using a timedelta that has more than one argument:
print("In two days and three weeks, it will be: " + str(now + timedelta(days=2, weeks=3)))

# Using a timedelta to work out a date from the past:
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago it was: " + s)

# Using a timedelta to work out how many days until April Fool's Day:
today = date.today()
afd = date(today.year, 4, 1)

if afd < today:
    print("April Fool's day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year = today.year+1)

time_to_afd = afd-today
print("It's only", time_to_afd.days, "days until April Fool's Day")