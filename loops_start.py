
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
    # This prints numbers 5 to 9 as Python
    # for loops are iterators and x represents the
    # individual value within the range.

    # Using a for loop over a collection:
    days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)
    # This prints each string (d) in the days array.

    # Using a break statement:
    for x in range(5, 10):
        if (x==7): break
        print(x)
    # This prints 5 and 6, then terminates the
    # loop as x equals 7.

    # Using a continue statement:
    for x in range(5, 10):
        if (x % 2 == 0): continue
        print(x)
    # This prints 5, 7 and 9, as the continue
    # statement only allows the print function to
    # to come into play when x is divisible by 2.

    # Using a loop with an index variable:
    days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i,d in enumerate(days):
        print(i, d)
    # This prints the index of the member of the
    # collection in question and the actual member.

if __name__ == "__main__":
    main()