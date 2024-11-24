# basic function
# Regular (Named) Functions
def add_numbers(a, b):
    return a + b


print(add_numbers(5, 5))

# Anonymous (Lambda) Functions
# small single expression functions used for one time use
add = lambda x, y: x + y  # Normal lambda function
print(add(5, 6))

listlambda = list(map(lambda x: x ** 2, [1, 2, 3, 4]))  # Using lambda with map
print(listlambda)

filterlamda = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # using lambda with filter
print(filterlamda)

students = [("Alice", 85), ("Bob", 75), ("Charlie", 90)]  # using lambda with sorted
sortedlambda = sorted(students, key=lambda students: students[1])
print(sortedlambda)

multiplelamda = lambda x, y, z: x * y * z
print(multiplelamda(1, 2, 3))

print((lambda x, y: x + y)(5, 3))


# YIELD
def race(arg):
    for i in range(arg):
        if i % 2 == 0:
            yield i


for i in race(20):
    print(i)


def count_up_to(num):
    count = 0
    while count <= num:
        yield count
        count += 1


for number in count_up_to(5):
    print(number)


# Recursive functions
def factorial(n):
    print(f"Calling factorial({n})")

    if n <= 1:
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"Computed factorial({n}) = {n} * factorial({n - 1}) = {result}")  # Shows the result at this step
        return result


# Testing the function
print("Final Result:", factorial(5))


# Higher-Order Functions
# Higher-order functions are functions that take other functions as arguments or return functions as results.
# In Python, functions like map, filter, and reduce are examples of higher-order functions.

def apply_func(func, x):
    return func(x)


print(apply_func(lambda x: x ** 2, 5))


def add_two_numbers(a, b):
    return a + b


def new_apply_func(func, a, b):
    return func(a, b)


print(new_apply_func(add_two_numbers, 5, 5))


# Nested Functions
# A nested function is a function defined inside another function.
# It is useful for encapsulating functionality that’s only relevant within the outer function.
# Nested functions can access variables from their enclosing scope, a concept known as a closure.

def add_2_number(a,b):
    def make_addition_inprivate():
        return a + b
    print("going inside inner method")
    return make_addition_inprivate()

print(add_2_number(4,4))

# Partial Functions (Using functools.partial)
# Partial functions are functions that have some arguments pre-filled,
# allowing you to create a new function with fewer arguments. This is done using functools.partial.

from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(2))  # Output: 10

# Method Functions

class Student: # class
    def __init__(self, name, rollno, marks): # Constructor, Intilizations first step
        self.name = name # instance variables
        self.rollno = rollno
        self.marks = marks

    def studentRecord(self): #instance method
        print("student name is {}".format(self.name))
        print("student roll no is {}".format(self.rollno))
        print("student marks are {}".format(self.marks))

    def calculate_perc(self):
        percentage = (self.marks/100)*100
        print("the percentage achieved by student {} is {}".format(self.name, percentage))

s = Student("akhil", "161392", 95)
s.studentRecord()
s.calculate_perc()

# Default arguments
# we can provide a default value while creating a function
def add_numbers(a,b=10):
    print(a+b)

add_numbers(5,15)
add_numbers(5)

# Keyword arguments
# we can provide arguments based on keys as weel with out following order
def multiplynumbers(a,b,c):
    print("a: ",a)
    print("b: ",b)
    print("c: ",c)
    print(f"multiplied value: {a*b*c}")

multiplynumbers(c=20, a=10, b=25)

# Required arguments
# when a input variable is there for the function or method it should be given for sure.
# if not provided it throws error

""" variable-length arguments """
#Arbitary arguments
def name(*name):
    print("Hello,", name[0], name[1], name[2])
    
name("james", "buchanan", "barnes")

# keyword arbitrary arguments

def kwname(**kwargs):
    print("HELLO, ", kwargs['fname'], kwargs["mname"], kwargs["lname"])

kwname(fname="akhil",mname="reddy", lname="matta")
