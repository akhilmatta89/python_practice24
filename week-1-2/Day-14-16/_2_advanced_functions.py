
# Function returning something
def adding_two_numbers(a,b): # Use the return statement to return a value from a function.
    return a+b
sum_of_2_numbers = adding_two_numbers(2, 3)
print(sum_of_2_numbers)

# Default Parameters:
# Assign default values to parameters.
# Allows calling function without providing arguments for parameters with defaults.

def org(org_name="UST"):
    print("The org name is {}".format(org_name))

org("TCS") # This prints what we have provided
org() # This prints the default value

# Arbitrary Arguments, *args or Variable-Length Arguments:
# If you do not know how many arguments that will be passed into your function,
# Add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
# Arbitrary Arguments are often shortened to *args in Python documentations.
#
def employee(*args): # If the number of arguments is unknown, add a * before the parameter name:
    a = "akhil","reddy","matta"
    print(type(a))
    print(args)
    print("My first name is", args[0])

employee("akhil",28, "UST")

def sum_numbers(*args):
    ttl_cnt = 0
    for i in args:
        ttl_cnt = ttl_cnt + i
    print(ttl_cnt)
sum_numbers(2,3,4,5,6)

# Keyword Arguments:
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def keyword_args(child1, child2, child3):
    print("my first child name is ", child1)
    print("my second child name is ", child2)
    print("my third child name is ", child3)

keyword_args(child2="akhil", child3="jaya", child1="reddy")

# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function,
#   add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

def employee_details(**employee):
    print(employee.get("name"))
    print(employee.get("age"))
    print(employee.get("org"))

employee_details(name="akhil",age=28,org="UST")
employee_details(name="jaya",org="LTI")

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
#   and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def print_fuits(fruits):
    print(type(fruits))
    for fruit in fruits:
        print(fruit)

fruits = ["apple","banana","cherry"]
print_fuits(fruits)

# function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.

def pass_function():
    pass
pass_function()

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:


# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, x):
  print(x)

my_function(x = 3)
try:
    my_function(3)
except:
    print("This will raise error")

##### Advanced concepts
# Lambda Functions:
# These are also called anonymous functions
# where we can add a functionality in a single line
# Lambda functions are meant to be concise, single-expression functions

square = lambda x: x ** 2
print(square(5))

is_apple_present = lambda fruits: any(x == "apple" for x in fruits) # # Using lambda with any()
print(is_apple_present(["banana","cherry", "apple"]))
print(is_apple_present(["banana","cherry"]))

is_apple_present_withfilter = lambda fruits: bool(list(filter(lambda  x:x=="apple", fruits)))
print(is_apple_present_withfilter(["banana","cherry", "apple"]))
print(is_apple_present_withfilter(["banana","cherry"]))



