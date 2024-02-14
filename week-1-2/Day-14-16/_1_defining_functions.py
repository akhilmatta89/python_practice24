"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
"""

def my_first_function():
    print("This is the way to create function")

my_first_function() # To call a function, use the function name followed by parenthesis:

# Arguments
"""
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. 
    You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). 
    When the function is called, we pass along a first name, 
    which is used inside the function to print the full name:
"""

def employee_first_name(fname:str):
    print(type(fname))
    print(f"Employee first name is {fname}")

employee_first_name("akhil")

# As i have mentioned argument type as string if other than that if i pass that will not raise any exception that just
# serve as documentation and hints for static type checkers, but they don't enforce type checking at runtime by default.
employee_first_name(26)
employee_first_name("Emil")
employee_first_name("Tobias")
employee_first_name("Linus")

# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Number of Arguments By default, a function must be called with the correct number of arguments. Meaning that if
# your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
print("---------------------------------------------------------------")
def employee_fullname(fname:str, lname:str):
    print("full name is :{} {}".format(fname,lname))

employee_fullname("akhil","reddy")
try:
    employee_fullname("akhil","reddy","matta") # when you sent more than arguments which is needed it raises exception
except Exception as ex:
    print(ex)
