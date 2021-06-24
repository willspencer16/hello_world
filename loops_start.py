
def main():
    x = 0

    # Defining a while loop:
    while (x<5):
        print(x)
        x = x+1
    # This will print x until its value is 5,
    # as a while loop executes a block of code
    # while a particular condition evaluates true.

    # Defining a for loop:
    for x in range(5, 10):
        print(x)
    # This prints numbers five to nine as Python
    # for loops are iterators and x represents the
    # individual value within the range.

    # Using a for loop over a collection
    days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)
    # This prints each string (d) in the days array.

if __name__ == "__main__":
    main()