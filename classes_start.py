
# Defining a class:
class myClass():
    def method1(self):
        print("myClass method1")
    
    def method2(self, someString):
        print("myClass method2 " + someString)

# Defining another class that inherits from the first:
class anotherClass(myClass):
    def method1(self):
        myClass.method1(self) # This calls the inherited method.
        print("anotherClass method1")
    
    def method2(self, someString):
        print("anotherClass method2 ")

# Instantiating the classes:
def main():
    c = myClass() # This instantiates an object instance of this class.
    c.method1() # Methods in the class can then be called like so.
    c.method2("This is a string") # Along with an argument passed in.

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is a string")
    # This argument doesn't get printed as it's not calling the inherited method.


if __name__ == "__main__":
    main()