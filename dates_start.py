
# Defining import statements:
from datetime import date
from datetime import time
from datetime import datetime

# Defining a function, calling the import function within:
def main():
    today = date.today()
    print("Today's date is ", today)

if __name__ == "__main__":
    main()