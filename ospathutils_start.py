# Working with os.path module:

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # Printing the name of the OS:
    print(os.name)

    # Checking for item existence and type:
    print("Item exists: " + str(path.exists("textfile.txt")))
    print("Item is a file: " + str(path.isfile("textfile.txt")))
    print("Item is a directory: " + str(path.isdir("textfile.txt")))

    # Working with file paths:
    print("Item path: " + str(path.realpath("textfile.txt")))
    print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))

if __name__ == "__main__":
    main()