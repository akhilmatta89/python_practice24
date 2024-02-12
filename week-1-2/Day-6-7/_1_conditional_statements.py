"""- Python supports the usual logical conditions from mathematics:
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""

# if statement example
fruit_a = "apple"
fruit_b = "apple"
if fruit_a == fruit_a:
    print("Both are same")

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 20
b = 30
if a > b:
    print(f"{a} is greater than {b} value")
elif b > a:
    print(f"{b} is greater than {a}")

# The else keyword catches anything which isn't caught by the preceding conditions.
a = 20
b = 30
if a > b:
    print(f"{a} is greater than {b} value")
elif b < a:
    print(f"{b} is greater than {a}")
else:
    print("Nothing has met")

# Short hand if
if a < b:print(f"{a} is less than {b} value")

# short hand if else
print(f"{a} is greater than {b} value") if a > b else print(f"{b} is greater than {a}")

# This short hand techniques is known as Ternary Operators, or Conditional Expressions.

# You can also have multiple else statements on the same line:
a = 30
b = 30
print("A") if a > b else print("=") if a == b else print("B")

# Now lets use some logical operator
a = 20
b = 30
c = 40
if a < b and b < c: # The and keyword is a logical operator, and is used to combine conditional statements:
    print(f"{a} is less than {b} and {b} is less than {c}")

if a > b or b < c: # The or keyword is a logical operator, and is used to combine conditional statements:
    print("One condition is satisfied")

# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
if not a > b:
    print(f"{a} is not greater than {b}")

# Nested IF
# You can have if statements inside if statements, this is called nested if statements.
if "apple".startswith("a"):
    if "apple".endswith("b"):
        print("apple is ending with b")
    else:
        print("Nothing.")

# pass statemnt
# if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.

if a < b:
    pass