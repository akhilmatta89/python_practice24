# Function returning something
def adding_two_numbers(a, b):  # Use the return statement to return a value from a function.
    return a + b


sum_of_2_numbers = adding_two_numbers(2, 3)
print(sum_of_2_numbers)


# Default Parameters:
# Assign default values to parameters.
# Allows calling function without providing arguments for parameters with defaults.

def org(org_name="UST"):
    print("The org name is {}".format(org_name))


org("TCS")  # This prints what we have provided
org()  # This prints the default value


# Arbitrary Arguments, *args or Variable-Length Arguments:
# If you do not know how many arguments that will be passed into your function,
# Add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
# Arbitrary Arguments are often shortened to *args in Python documentations.
#
def employee(*args):  # If the number of arguments is unknown, add a * before the parameter name:
    a = "akhil", "reddy", "matta"
    print(type(a))
    print(args)
    print("My first name is", args[0])


employee("akhil", 28, "UST")


def sum_numbers(*args):
    ttl_cnt = 0
    for i in args:
        ttl_cnt = ttl_cnt + i
    print(ttl_cnt)


sum_numbers(2, 3, 4, 5, 6)


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


employee_details(name="akhil", age=28, org="UST")
employee_details(name="jaya", org="LTI")


# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
#   and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def print_fuits(fruits):
    print(type(fruits))
    for fruit in fruits:
        print(fruit)


fruits = ["apple", "banana", "cherry"]
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


my_function(x=3)
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

is_apple_present = lambda fruits: any(x == "apple" for x in fruits)  # # Using lambda with any()
print(is_apple_present(["banana", "cherry", "apple"]))
print(is_apple_present(["banana", "cherry"]))

is_apple_present_withfilter = lambda fruits: bool(list(filter(lambda x: x == "apple", fruits)))
print(is_apple_present_withfilter(["banana", "cherry", "apple"]))
print(is_apple_present_withfilter(["banana", "cherry"]))

is_banana_present = lambda fruits: print("yes banana is present") if "banana" in fruits else print("Not present")
is_banana_present(["banana", "cherry", "apple"])

is_banana_present = lambda fruits: "yes banana is present" if "banana" in fruits else "Not present"
return_stat = is_banana_present(["banana", "cherry", "apple"])
print(return_stat)

perform_multiplication = lambda a, b: print(a * b)
perform_multiplication(2, 3)

print("codewars example -----------------------------")
sheep = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

def count_sheeps(sheep):
  # TODO May the force be with you
    increment_count = lambda sheep: len(list(filter(lambda x: x == True, sheep)))
    true_count = increment_count(sheep)
    return true_count
print(count_sheeps(sheep))

def count_sheeps_1(sheep):
    return sheep.count(True)

print(count_sheeps_1(sheep))
print("codewars example -----------------------------")
##### High Order functions
# Functions that take other functions as arguments or return functions

def addition(a, b):
    return a + b

def apply(func, a, b):
    return func(a, b)

result = apply(addition, 2, 3)
print(result)


###### Closures

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
result = closure(5)  # Adds 10 (captured from outer_function) and 5
print(result)


def normal_starting_text(x):
    def name(y):
        return x + y
    return name
nrmlfunc = normal_starting_text("My Name is ")
my_str = nrmlfunc("AKHIL")
print(my_str)


###### Decorators
# Functions that modify or enhance other functions

def smart_div(func):
    def inner(a, b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner

@smart_div
def div(a, b):
    return a/b
print(div(2,4))

# Define custom exception class
class UnauthorizedError(Exception):
    pass

def my_auth_validator(func):

    def inner(request_json):
        if request_json.get("auth") == "P@ssw0rd":
            return func(request_json)
        else:
            raise UnauthorizedError
    return inner

@my_auth_validator
def api_function(request_json):
    save_to_db(request_json)

def save_to_db(request_json):
    print("saving employee name", request_json.get("name"))
    print("saving employee salary", request_json.get("salary"))

request_json = {"name":"akhil","age":28, "auth":"P@ssw0rd"}
api_function(request_json)

request_json = {"name":"akhil","age":28, "auth":"P@ssw0rd"} # If you chnage the auth it throws error
api_function(request_json)


###### Generator Functions:
# Functions that use the yield keyword to produce a sequence of values lazily.
def func1():
    return 1
    return 2
    return 3
print("_________________using return")
print(func1()) # Here normal return function only returns one return statement
# To return multiple returns we use yield keyword
def func2():
    yield 1
    yield 2
    yield 3
print("_________________using yield")
rslt = func2()
for i in rslt:
    print(i)

def func3():
    for i in range(6):
        yield i
print("_________________using yield")
for i in func3():
    print(i)
print("_________________using yield")
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)

rslt = countdown(5)
print(rslt)
print(rslt.__next__())
print(rslt.__next__())
print(rslt.__next__())
