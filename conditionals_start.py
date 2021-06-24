
# Defining a function with two variables and a conditional flow:
def main():
    x, y = 100, 100

    if (x < y):
        st = "x is less than y"
    elif (x == y):
        st = "x is the same as y"
    else:
        st = "x is greater than y"

    print(st)

# Depending on whether the x variable is greater or less than y, the correct string
# is printed accordingly. If the variables are the same, however, without the elif,
# the last string is printed, as Python evaluating the first conditional to be false
# and defaults to the else.

# Using a conditional statement:
    st = "x is less than y" if (x < y) else "x is greater than or the same as y"
    print(st)

# This lets you write a common if else statement all in one line.

if __name__ == "__main__":
    main()