# Importing the calendar module:
import calendar

# Creating a plain text calendar:
c = calendar.TextCalendar(calendar.SUNDAY) # Whatever day is specified here, is the day the calendar starts with.
st = c.formatmonth(2021, 1, 0, 0)
print (st)

# Creating an HTML formatted calendar:
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2021, 1)
print (st)
# This prints out the html code to create the calendar.

# Looping over the days of a month:
for i in c.itermonthdays(2021, 8):
    print(i)
# This prints of the numbers that represent each day of the month.
# There are zeros at the start and the end because there are days
# in that week which belong to another month.