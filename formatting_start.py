# Using predefined string control codes:

from datetime import datetime

# Using the predefined string control to show the current year:
def main():
    now = datetime.now()
    print(now.strftime("The current year is: %Y"))

    # Using several predefined string control codes:
    print(now.strftime("%a, %d %B, %y"))
    # This prints the abbreviated day name, followed
    # by the day of the month and a full month name,
    # with an abbreviated two-digit year.

    # Printing in the current locale's formatting:
    print(now.strftime("locale date and time: %c"))
    print(now.strftime("locale date: %x"))
    print(now.strftime("locale time: %X"))

    # Using the predefined string control codes to format the time:
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24-hour time: %H:%M"))

if __name__ == "__main__":
    main()