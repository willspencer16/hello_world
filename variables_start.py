
# Declare a variable and initialize it
f=0
# print(f)

# # Re-declaring the variable
# f="abc"
# print(f)

# # ERROR: variables of different types cannot be combined
# print("this is a string " + str(123))

# Global vs. local variables in functions
def someFunction():
    global f
    f='def'
    print(f)

someFunction()
print(f)

del f #undefines the variable
print(f)