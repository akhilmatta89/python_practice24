# In this file i will do operations on string whereas if you want to know the basics of string please go and refer
# _3_datatypes.py file for basics

# In Python, you can perform various operations on strings. Here are some common string operations with examples:

# Strings are arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# from the strating of the string the index value is 0
# from the end of the string the index value is -1

a = "Hello world"
print("iam getting first value of the string", a[0])
print("iam getting last value of the string", a[-1])

# Looping through a string
# Since strings are arrays we can loop through it.

fruit = 'banana'
for char in fruit:
    print(char)

# we can get the string length as well
print("The length of above mentioned fruit is", len(fruit))

# To get the certail phrase or character present in the string we use "in" a keyword and it returns bool value
descp = "My name is akhil and iam from hyd"
print("akhil" in descp)

# we can also perform some conditionals in it
if "akhil" in descp:
    print("yes akhil is in the descp")

# checking if not

print("jaya" not in descp)

if "jaya" not in descp:
    print("yes jaya is not in descp")

print("------------------------------------------- slicing ----------------------------------------------------")
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

b = "Hello, World!"  # Get the characters from position 2 to position 5 (not included):
print(b[2:5])

# Slicing from starting
print(b[:5])

# Slicing to the end
print(b[2:])

# Negative indexing
print(b[-6:-1])

# Slicing with step value.
print(b[0:13:2])

# Reversing a string
print(b[::-1])
print(b[1::])

# Using slice object
my_str = "Python Programming"
my_slice = slice(5, 16)
print(my_str[my_slice])

# Skipping elements
print(my_str[::3])
print(my_str[::-3])

# Combining Slicing with Other String Operations:
formatted_output = f"when i performed slicing with skipping for every 3 elemnts from starting of the string " \
                   f"the value is {my_str[::3]}, from the end the value is {my_str[::-3]}"
print(formatted_output)

# Using slicing in a loop:
for i in range(0, len(my_str), 3):
    print(my_str[i:i + 3])

# Conditional Slicing:
my_string = "ABCDEFGHIJKL"
cond = True
print(my_string[:5] if cond else my_string[5:])

# Splitting a String:
print(my_string.split())
splitted_txt = formatted_output.split()
print(splitted_txt)

# Joining the splitted text
joined_text = " ".join(splitted_txt)
print(joined_text)

# Reversing the words in a string.
reversed_text = " ".join(reversed(joined_text.split()))
print(reversed_text)

# Padding the strings
stringpad = "akh"
print(stringpad.ljust(5, "i"))
print(stringpad.rjust(5, "a"))

# Trimming the white spaces.
text = "    akhil reddy   "
print(text.strip())

# The upper() method returns the string in upper case:
print(text.strip().upper())

# The lower() method returns the string in lower case:
text = "Hello World"
print(text.lower())

# String concatenation
a = "Hello"
b = " world"
print(a + b)  # Basic Concatenation
print(a + b, " welcome to the programming world")  # concatenation with variables
print("{}, welcome to the programming world".format(a + b))  # Using format method
print(f"{a + b}, welcome to the programming world")  # Using f string
words = ["Hello", "world"]
print("".join(words))  # Joining strings from list
print("abc"*2)  # Concatenation with repeat
result = "Hello"
result += " world"  # Using += for In-Place Concatenation:
print(result)

# Format strings
age = 36
try:
    txt = "My name is John, I am " + age
    print(txt)  # Basic formatting , But this gives error as we are concatenating string and int.
except Exception as ex:
    print("Obviously this throws error")

# Best way to concat string and int is using format method.
txt = "My name is John, I am {}".format(age)
print(txt)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno, price))

# We can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity,itemno, price))

# Escape Characters

# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:


try:
    # txt = "We are the so-called "Vikings" from the north."
    txt = "We are the so-called \"Vikings\" from the north."
    print(txt)
except Exception as ex:
    print("with out back slash, below is the error", ex)

# If you have single quote you can add single back slash

print('it\'s already 10 AM')
print("This will insert one \\ backslash")

# Too get into the new line use \n

print("my name is akhil\niam learning python")
print("Hello\rWorld!")

# To add a tab in print statement
print("iam akhil\tiam learning python")

# To give one back space back we use \b
print("iam akhil \biam learning python")
