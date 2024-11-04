# This has all the string methods

"""------------------------FORMAT----------------------------"""
name = "akhil"
print("my name is {}".format(name))  # .format is used when we want to use formatted strings
print("my salary is {} and i work for {}".format(90000, "UST"))

place = "Hyderabad"
print("i stay in %s from more than %d" % (place, 8))

"""------------------------REPLACE----------------------------"""
name = "akhil"
name = name.replace("a", "r")  # Replace method replaces the substring from the string
print(name)

name = 'my name is akhil'
name = name.replace("akhil", "reddy")
print(name)

name = "akhil"
name = name.replace("akhil", "reddy")
print(name)

"""------------------------MAKETRANS----------------------------"""
trans_tab = str.maketrans("a", "@")  # can translate the characters with the given string
name = "akhil"
print(name.translate(trans_tab))

transtab = str.maketrans({"a": "r"})
print("my name is akhil reddy and people call me akhil".translate(transtab))

"""------------------------SWAPCASE----------------------------"""
# swapcase is used to convert the case of either string or the sentence
# It converts to the opposite state

name = "akhil"
print(name.swapcase())

up_name = "AKHIL"
print(up_name.swapcase())

info = "My Name Is Akhil Reddy"
print(info.swapcase())

"""------------------------ENDSWITH----------------------------"""
# Returnd bool value if the specified string/char ends/not ends with it
# case sensitive

name = "akhil"
print(name.endswith("l"))
print(name.endswith("r"))

info = "My Name Is Akhil Reddy"
print(info.endswith("Reddy"))
print(info.endswith("reddy"))

"""------------------------STARTSWITH----------------------------"""
# Returnd bool value if the specified string/char starts/not starts with it
# case sensitive

name = "akhil"
print(name.startswith("a"))
print(name.startswith("b"))

info = "My Name Is Akhil Reddy"
print(info.startswith("My"))

"""------------------------INDEX----------------------------"""
# Returns the index of the char/ word in the entire string
# If duplicates present returns the first value
# Can also specify start and end of the string

name = "akhil"
print(name.index("a"))
print(name.index("l"))

name = "reddy"
print(name.index("d"))

print("my name is akhil reddy and people call me akhil".index("akhil"))

print("my name is akhil reddy and people call me akhil".index("akhil", 16, 47))

"""------------------------COUNT----------------------------"""
# Returns number of time the word/char has found in the entire string
# Can also specify start and end of the string

name = "akhil is akhil"
print(name.count("akhil"))

print(name.count("akhil", 0, 6))

"""------------------------ZFILL----------------------------"""
# The zfill() method in Python pads a string on the left with zeros (0) until it reaches the specified width.

name = "akhil is akhil"
print(name.zfill(20))

"""------------------------TITLE----------------------------"""
# Captilizes the first char in each every word of the string
name = "akhil is akhil"
print(name.title())

"""------------------------SPLITLINES----------------------------"""
# splitlines method is used to split the words accordingly as per escape sequences
# Splits by line breaks (\n, \r, \r\n)
name = "akhil\nis\nakhil"
print(name.splitlines())

text = "Hello\nWorld\nWelcome to Python"
print(text.splitlines())

text = "Hello\nWorld\nWelcome to Python"
print(text.splitlines(False))

"""------------------------SPLIT----------------------------"""
# split() will split the string at any whitespace by default.
# Splits a string into a list based on a specified separator (default is any whitespace)
name = "Akhil"
print(name.split())

info = "My name is akhil"
print(info.split())

"""------------------------STRIP----------------------------"""
# Removes white spaces from the start and end of the string
name = " akhil      "
print(name.strip())

"""------------------------RSTRIP----------------------------"""
# Removes white spaces from the right side of the string
# if anything is given as input tries to remove those occurrences

name = "akhil        "
print(name.rstrip())

text = "Hello, World!!!"
print(text.rstrip("!"))

text = "Hello, World!!!"
print(text.rstrip("@"))

text = "Hello, World?!?"
print(text.rstrip("!?"))

"""------------------------LSTRIP----------------------------"""
# Removes white spaces from the left side of the string
# if anything is given as input tries to remove those occurrences

name = "     akhil    "
print(name.lstrip())

name = "@@@akhil@@@"
print(name.lstrip("@"))

name = "@@@akhil@@@"
print(name.lstrip("!"))

name = "@@@!akhil@@@!"
print(name.lstrip("!@"))

"""------------------------RJUST----------------------------"""
# The rjust() method in Python is used to right-align a string by padding it with a
# specified character (default is a space) on the left, until it reaches a specified width
# if width specified is less than the string length nothing happens
name = "akhil"
print(name.rjust(20))

name = "akhil"
print(name.rjust(20, "@"))

name = "akhil"
print(name.rjust(3,"@"))

"""------------------------LJUST----------------------------"""
# The ljust() method in Python is used to left-align a string by padding it with a
# specified character (default is a space) on the right, until it reaches a specified width
# if width specified is less than the string length nothing happens
name = "akhil"
print(name.ljust(20))

name = "akhil"
print(name.ljust(20,"@"))

name = "akhil"
print(name.ljust(3,"!"))

"""------------------------RFIND----------------------------"""
# The rfind() method in Python searches for the last (rightmost) occurrence of a specified substring within a string.
#  It returns the index of the start of the substring if found, or -1 if the substring is not found.
name = "akhikl"
print(name.rfind("k"))

name = "akhikl"
print(name.rfind("@"))

text = "Hello, world! Welcome to the world of Python."
index = text.rfind("world", 0, 25)
print(index)

text = "Hello, world!"
index = text.rfind("o")
print(index)  # Output: 8

text = "ababab"
index = text.rfind("ab")
print(index)

"""------------------------RPARTITION----------------------------"""
# The rpartition() method in Python splits a string into three parts,
# based on the last occurrence of a specified separator.
comapny = "UST-GLOBAL"
print(comapny.rpartition("-"))

name = "ak-hik-l"
print(name.rpartition("-"))

text = "Hello, world! Welcome to Python."
result = text.rpartition(" ")
print(result)


"""------------------------PARTITION----------------------------"""
# The partition() method in Python splits a string into three parts,
# based on the first occurrence of a specified separator.
name = "ak-hik-l"
print(name.partition("-"))

comapny = "UST-GLOBAL-inc"
print(comapny.partition("-"))

text = "Hello, world! Welcome to Python."
result = text.partition(" ")
print(result)

"""------------------------JOIN----------------------------"""
# The join() method in Python is used to concatenate elements of an iterable (like a list or tuple)
# into a single string, with each element separated by a specified delimiter. It’s often used to
name = "akhil"
print(name.join(["Hello", "world"]))

info = ["welcome","to","akhil's","world"]
print(",".join(info))

des = ["Heelo", "world", "from", "python"]
print("-".join(des))

"""------------------------ISNUMERIC----------------------------"""
#The isnumeric() method in Python checks if all characters in a string are numeric characters. If all characters are numeric,
# it returns True; otherwise, it returns False.
# Includes digits, Unicode numeric characters, superscripts, and fractions.
name = "akhil"
print(name.isnumeric())
print(str.isnumeric(name))

count = "20"
print(count.isnumeric())

unicodestr = "\u2155"
print(unicodestr.isnumeric())

s = "-123"
print(s.isnumeric())  # Output: False

s = "3.14"
print(s.isnumeric())  # Output: False

"""------------------------ISDECIMAL----------------------------"""
"""The isdecimal() method only returns True for characters that 
    represent basic decimal digits (0–9) and does not recognize:

Subscript or superscript numbers (e.g., ², ³)
Unicode fractions or numeric characters (e.g., ⅕)
Symbols, letters, whitespace, or punctuation
Negative signs or decimal points
"""
count = "1.3"
print(count.isdecimal())

s = "12345"
print(s.isdecimal())  # Output: True

s = "²"
print(s.isdecimal())  # Output: False

s = "\u2155"  # Unicode for ⅕
print(s.isdecimal())  # Output: False

"""------------------------ISDIGIT----------------------------"""
"""Method	Recognized Characters
isdigit()	Basic digits (0-9), superscripts, subscripts, Unicode digits
isdecimal()	Decimal numbers (0-9, some non-ASCII decimals)
isnumeric()	Decimal numbers, Unicode fractions, subscripts, superscripts"""

count = "1.3"
print(count.isdigit())

s = "²"
print(s.isdigit())

u = "\u2155"  # Unicode for ⅕
print(u.isdigit())

"""------------------------ISPRINTABLE----------------------------"""
"""
The isprintable() method in Python checks if all characters in a string are printable. If every character 
in the string is printable, it returns True; otherwise, it returns False

Printable characters include letters, digits, punctuation, and whitespace
 (like spaces and tabs). 
 
 Non-printable characters include control characters 
 (such as newline and carriage return) and other non-visible characters.
"""
name = "akhil"
print(name.isprintable())

name = "akhil\nreddy"
print(name.isprintable())


"""------------------------ISTITLE----------------------------"""
# Return True if the string is a title-cased string, False otherwise.

name = "akhil"
print(name.istitle())

name = "Akhil"
print(name.istitle())

"""------------------------ISIDENTIFIER----------------------------"""
# Return True if the string is a valid Python identifier, False otherwise.
name = "akhil"
print(name.isidentifier())

idf_1 = "akhil-123"
print(idf_1.isidentifier())

idf_2 = "123akhil"
print(idf_2.isidentifier())

"""------------------------ISSPACE----------------------------"""
# Return True if the string is a whitespace string, False otherwise.
name = "akhil"
print(name.isspace())

name = "akhil Reddy"
print(name.isspace())

name = " "
print(name.isspace())

"""------------------------ISUPPER----------------------------"""
# Return True if the string is an uppercase string, False otherwise.
name = "akhil"
print(name.isupper())

name = "AKHIL"
print(name.isupper())

name = "Akhil"
print(name.isupper())

"""------------------------ISLOWER----------------------------"""
# Return True if the string is an lowercase string, False otherwise.
name = "akhil"
print(name.islower())

name = "Akhil"
print(name.islower())

"""------------------------ISALNUM----------------------------"""
# Return True if the string is an alpha-numeric string, False otherwise.
name = "akhil"
print(name.isalnum())

name = "akhilqw123"
print(name.isalnum())

name = "123"
print(name.isalnum())

name = "@"
print(name.isalnum())

"""------------------------ISASCII----------------------------"""
# Return True if all characters in the string are ASCII, False otherwise.
name = "akhil"
print(name.isascii())

s = "Café"  # Contains an accented character 'é'
print(s.isascii())  # Output: False

"""------------------------FORMAT_MAP----------------------------"""
# The format_map() method in Python is used to format strings by
#   replacing placeholders with values from a dictionary.
data = {'name': 'Alice', 'age': 30}
formatted_string = "My name is {name} and I am {age} years old.".format_map(data)
print(formatted_string)

data = {'person': {'name': 'Eve', 'age': 22}}
formatted_string = "My name is {person[name]} and I am {person[age]} years old.".format_map(data)
print(formatted_string)

"""------------------------FIND----------------------------"""
"""
Feature	str.index()	str.find()
Return Value	Index of first occurrence or raises ValueError	Index of first occurrence or returns -1
Error Handling	Raises an error if not found	Returns -1 if not found
"""
name = "akhkil"
print(name.find("k"))

name = "akhkil"
print(name.index("k"))

"""------------------------EXPANDTABS----------------------------"""
# The expandtabs() method in Python is used to replace tab characters (\t) in a string with spaces. By default,
# it converts each tab character into a series of spaces,
name = "akhkil\tReddy"
print(name.expandtabs())

name = "akhkil\tReddy"
print(name.expandtabs(tabsize=16))

"""------------------------CENTER----------------------------"""
# Return a centered string of length width.
# Padding is done using the specified fill character (default is a space).

name = "akhil"
print(name.center(20))

name = "akhil"
print(name.center(20,"-"))

"""------------------------CASEFOLD----------------------------"""
# The casefold() method in Python is used to convert a string to lowercase in a way that is more aggressive than lower()
# t is designed for case-insensitive comparisons,
name = "Akhil"
print(name.casefold())

"""------------------------CAPITALIZE----------------------------"""
# Return a capitalized version of the string.
# More specifically, make the first character have upper case and the rest lowercase.

name = "akhil reddy"
print(name.capitalize())


"""------------------------ENCODE----------------------------"""
# The encode() method in Python is used to convert a string into a specified encoding, typically transforming it
# into a bytes object. This is essential when dealing with text in different encodings, such as UTF-8, ASCII,
name = "akhil reddy"
print(name.encode())

name = "akhil reddy"
print(name.encode(encoding="ASCII"))

"""------------------------ISALPHA----------------------------"""
# Return True if the string is an alphabetic string, False otherwise.
name = "akhilreddy"
print(name.isalpha())

name = "123"
print(name.isalpha())

"""------------------------REMOVEPREFIX----------------------------"""
name = "akhil rEDDY"
print(name.removeprefix("akhil"))

"""------------------------REMOVESUFFIX----------------------------"""
name = "akhil rEDDY"
print(name.removesuffix("rEDDY"))

"""------------------------RIndex----------------------------"""
# returns the index of the last repeated character
name = "akhkikl"
print(name.rindex("k"))

"""------------------------RSPLIT----------------------------"""
# splits from the right side
name = "akh-kikl"
print(name.rsplit("-"))

