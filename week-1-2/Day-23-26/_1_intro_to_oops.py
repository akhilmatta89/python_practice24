"""
Python Classes/Objects
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
Almost every thing in python are objects
class :- blueprint/plan/design
object :- physical existence of class is nothing but object
reference variable :- the variable which can be used to refereing to an object.
                        by using reference variable swe can access properties and methods of an object

we have 3 types of variable
    - instance variables
    - static variables
    - local variables

we have 3 types of methods in oops concepts
    - instance method
    - static method
    - class method
"""


# Example of a class with lame example
# write a program to creeate a student class and create an object to it call the method to display details
class Student:
    """This is the employee class"""

    def __init__(self):  # Constructor, this is the magic method which calls first when evr class is intialized
        print("As iam __init__ method i will be called first whenever class is intialized")
        self.name = "akhil"  # intilaizing the variables
        self.age = 28
        self.marks = 80

    def impl(self):
        print("my name is: ", self.name)  # making use of intilaizing the variables
        print("my age is: ", self.age)
        print("my marks are: ", self.marks)


e = Student()
print(e.__doc__)  # we can print doc string by using this method
print(help(e))  # we can also print doc string by using help as well
print(e.name)  # Calling the variables directly using reference variable
print(e.marks)
print(e.age)
e.impl()

"""
diff between method and constructor
    - method is user defined, constructor is pre-defined
    - method call should be done manually, constructor call is automatic(when class is intialized)
    - per object method can be called any number of times, constructor call happens only once while initializing
    - inside method we can write logic, inside constructor we have to declare and intilaize instance variables
"""

# Types of variables
"""
    - Instance variables
    - static variables
    - local variables
"""
