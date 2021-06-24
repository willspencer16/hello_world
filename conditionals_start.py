
# Defining a function with two variables:
def main():
    x, y = 100, 100

    if (x < y):
        st = "x is less than y"
    elif (x == y):
        st = "x is the same as y"
    else:
        st = "x is greater than y"

    print(st)

# Depending on whether the x variable is
# greater or less than y, the correct string
# is printed accordingly. If they are the same,
# however, the last string is printed, as Python
# evaluating the first conditional to be false

if __name__ == "__main__":
    main()