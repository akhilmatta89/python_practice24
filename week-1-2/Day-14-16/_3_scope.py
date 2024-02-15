"""
The scope of a function in Python defines the visibility and accessibility of variables and other identifiers
    within the function.
Understanding function scope is crucial for writing maintainable and bug-free code.
Here's an explanation of the scope of functions in Python:

"""

#### Local Scope:
"""
Variables defined inside a function are considered to be in the local scope.
They are only accessible within the function where they are defined.
Local variables are created when the function is called and destroyed when the function exits.
"""
x = 15
def func1():
    x = 10 # Local Variable
    print(x) # This prints 10 takes the local variable
func1()
print(x) # This will not return 10 instaed takes global variable

def func2():
    print(x) # This prints the global variable
func2()


#### Enclosing (Nonlocal) Scope:
"""
If a function is defined inside another function, it can access variables from the outer function's scope.
Variables in the enclosing scope are not local to the inner function but are not global either.
Use the nonlocal keyword to modify variables from the enclosing scope.
"""

def outer_func():
    x = 20
    def inner_func():
        nonlocal x
        print("inner x value: ", x)

    inner_func()
    print("outer x value: ", x)

outer_func()


#### Global Scope:
"""
Variables defined outside of any function or in the global scope.
They are accessible from any function within the module.
Use the global keyword to modify global variables from within a function.
"""

x = 24
def my_func():
    # print("This is the global variable ", x) # This is the global variable
    # Now iam converting to global inside my func
    global x
    x = x+6
    print("This is my x where i used global keyword ", x)

my_func()
print("There will be  change in main global variable it should be 24 before but now it is ", x)

#### Built-in Scope:
"""
Python comes with a set of built-in functions and constants that are always accessible.
Examples include print(), len(), sum(), etc.
"""
def my_function():
    print(len("Hello"))  # Accessing built-in len() function

my_function()  # Output: 5


"""
Important Notes:
Variables in the innermost scope take precedence. If a variable with the same name exists in both the 
    local and global scopes, the local variable is used.
Avoid modifying global variables within functions unless necessary to maintain code clarity.
Using global variables excessively can make code hard to understand and debug. 
It's often better to pass variables as arguments to functions.
"""
