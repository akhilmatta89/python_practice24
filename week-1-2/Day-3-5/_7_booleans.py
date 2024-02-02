# Booleans represent one of two values: True or False.

"""In programming you often need to know if an expression is True or False.
You can evaluate any expression in Python, and get one of two answers, True or False.
When you compare two values, the expression is evaluated and Python returns the Boolean answer:"""


# This is the normal way where we are seeing the boolean values
print(10>9)
print("akhil" == "reddy")
print(2 > 4)

# When you run a condition in an if statement, Python returns True or False:
def comparer(a, b):
    if a > b :
        print("yes 10 is greater than 9")
    else:
        print("wrong calculation")

comparer(10,9)
comparer(9,10)

# The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(20))
print(bool(False))

"""
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""
print(bool(""))
print(bool(0))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

"""
One more value, or object in this case, evaluates to False, 
and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
"""
class Employee():
    def __init__(self, name, age, org, exp):
        self.name = name
        self.age = age
        self.org = org
        self.exp = exp

    def __len__(self):
        return 0

    def info(self):
        print(self.name)
        print(self.age)
        print(self.org)
        print(self.exp)

emp = Employee("akhil",28,"UST",4)
print(bool(emp))
emp.info()

# You can create functions that returns a Boolean Value:

def bool_returner():
    return True

x = bool_returner()
print(x)

def cond_bool():
    if bool_returner():
        print("Yes")
    else:
        print("No")

cond_bool()


# Python also has many built-in functions that return a boolean value, like the isinstance() function,
# which can be used to determine if an object is of a certain data type:

print(isinstance("Yes",str))

