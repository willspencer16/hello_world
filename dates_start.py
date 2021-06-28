
# Defining import statements:
from datetime import date
from datetime import time
from datetime import datetime

# Defining a function, calling the imported function within:
def main():
    today = date.today()
    print("Today's date is ", today)

    # Extracting specific components:
    print("Date components: ", today.day, today.month, today.year)

    # Using the weekday component:
    print("Today's weekday # is: ", today.weekday())
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print ("Which is a: ", days[today.weekday()])

    # Using the now function:
    today = datetime.now()
    print("The current date and time is ", today)

    # Getting the current time:
    t = datetime.time(datetime.now())
    print("The current time is ", t)

if __name__ == "__main__":
    main()