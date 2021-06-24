# Defining a function:
def func1():
    print("I am a function")

#Calling the function:
func1()
# Function is being called,
# therefore prints the string.

#Printing the function:
print (func1())
# Function doesn't return a value,
# so Python evaluates the return value
# to be the Python constant of none 
# and prints the string representation of that.

#Printing the value of the function:
print (func1)
# Function is not being executed
# due to the lack of parentheses.
# Instead it prints the value
# of the function definition itself.

# This shows the functions themselves are objects,
# which can be passed around to other pieces of Python code.

# Defining a function that takes arguments:
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# Defining a function that returns a value
def cube(x):
    return x*x*x

# Calling the function with arguments:
func2(10,20)
# This prints 10 and 20 with a space inbetween,
# as defined in the function.

# Printing the function with arguments:
print (func2(10,20))
# This prints 10 and 20 with a space inbetween,
# plus the Python constant of none, as the 
# function still does not return a value.

#Printing the function with a value:
print (cube(3))
# This prints the result of 3 cubed (27),
# without the Python constant of none, as
# there is a return within the function.
