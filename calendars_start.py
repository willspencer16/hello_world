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