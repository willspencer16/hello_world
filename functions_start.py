# Defining a function
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