# Note: All string methods return new values. They do not change the original string.

# Captilize :- The first character is converted to upper case, and the rest are converted to lower case
print("akhil".capitalize())
print("jaya is a MAD GIRL".capitalize())
print("36 is my age.".capitalize())

# Casefold :- The casefold() method returns a string where all the characters are lower case.
"""
This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, 
meaning that it will convert more characters into lower case, and will find more matches when comparing two strings 
and both are converted using the casefold() method.
"""
print("AKHIL".casefold())


# Center :- The center() method will center align the string, using a specified character (space is default) as the fill character.
print("AKHIL".center(20))
print("AKHIL".center(20,"a"))

# Count:- The count() method returns the number of times a specified value appears in the string.
# You also search in some part of the string by giving its start and end of the index.
txt = "akhil is a good boy akhil has good knowledge in python"
print(txt.count("akhil"))
print(txt.count("akhil", 20, 40))

# encode :- The encode() method encodes the string, using the specified encoding.
# If no encoding is specified, UTF-8 will be used.
txt = "My name is akhil"
x = txt.encode()
print(x)
print(type(x))

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

# endswith :- The endswith() method returns True if the string ends with the specified value, otherwise False.

txt = "my name is akhil"
print(txt.endswith("akhil"))
print(txt.endswith("jaya"))
print(txt.endswith("my world.", 5, 11)) # we can also give start and end of the string


# expandtabs :- used to give ttab spaces, if nothing is given default size is 8 characters is assumed
txt = "my \tname \tis\t akhil"
print(txt.expandtabs())
print(txt.expandtabs(2))

# format :- this inbuilt function is used to format the string in the specific way which we wanted
# we can also give our inputs inside the placeholders
name = "akhil"
age = 28
print("my name is {}".format(name))
print("my name is {} and my age is {}".format(name,age))
print("iam of age {ae}, and my name is {nme}".format(nme=name, ae=age))
print("iam of age {1}, and my name is {0}".format(name, age))

# find methods finds for the character in the string and returns its index
# it is not going to throw any error if the character i snot present in the string
# This is same like index method but index throws error if the character is not present
txt = "Hello world!"
print(txt.find("world",0,12))
print(txt.find("akhil"))
print(txt.find("z"))

#Format_map = this method is also same as format methid but we can map the values here
#The format_map method in Python is used to format a string using a mapping of key-value pairs.
# It's similar to the format method, but instead of passing arguments directly,
# you provide a dictionary or any other mapping object.

mapping = {"name":"akhil","age":28,"org":"UST"}
descp = "my name is {name}, and my age is {age}, and i work in {org}"
print(descp.format_map(mapping))

my_txt = descp.format_map(mapping)

# Index:- index method finds for the character in the string and returns its index
# if the character is not present in the string it returns back the error
# we can also give start and end of the string where you want to check
print(my_txt.index("akhil"))
print(my_txt.index("akhil",0,20))

try:
    my_txt.index("z")
except Exception as ex:
    print("Obviously this throws errors because index methid returns error id char is not present")

# isascii:- this method returns boolean values if the string has ascii characters in it
print(my_txt.isascii())
tst = "你好"
print(tst.isascii())

#isalnum ;- This string method returns true if the string has values with (a-z), (0,9), (A-Z)
# observation = spaces are not included this works only with a single word

isalnum_tst = "Akhilhas28age"
print(isalnum_tst.isalnum()) # This returns true
print(my_txt.isalnum()) # This returns false

# isdigit method returns boolean value if the string has digits in it
# Unicode characters also comes into picture

isdigit_tst = "123"
print(my_txt.isdigit()) # This returns false
print(isdigit_tst.isdigit()) # This returns true

# islower method returns boolean value if the string is lower in case
# if number is given as text it returns false
name ="akhil"
signs = "@#$%6"
print(my_txt.islower())
print(name.islower())
print(isdigit_tst.islower())
print(signs.islower())

# isupper method returns boolean value if the string is upper in case
# if number is given as text it returns false
name ="AKHIL"
print(name.isupper())
print(signs.isupper())
print(isdigit_tst.isupper())

# isspace :- Return True if the string is a whitespace string, False otherwise.
name = "      "
print(name.isspace()) # This returns true
name="akhil"
print(name.isspace()) # This returns false

#
# The isdecimal() method returns True if all the characters are decimals (0-9).
# This method can also be used on unicode objects.
my_num = "2"
print(my_num.isdecimal())

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())

# isidentifier is a method which returns if the text is of good format specifying identifier rules
print("identifier".isidentifier())
print("this_identifier".isidentifier())
print("iam_akhil_1".isidentifier())
print("2_akhil".isidentifier())


# isprintable :- The isprintable() method returns True if all the characters are printable, otherwise False.
# Example of none printable character can be carriage return and line feed.
print(my_txt.isprintable())
txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)

# isnumeric :- The isnumeric() method returns True if string contains number format, otherwise False.
name ="akhil"
print(name.isnumeric())
print("123".isnumeric())

# istitle :- istitle method returns True if the string is of title type means every start of the word should be capital
print(name.istitle())
title = "My Name Is Akhil"
print(title.istitle())

# Join methods joins 2 string
# The join() method takes all items in an iterable and joins them into one string.
my_tup = ("akhil","reddy","matta")
my_sign = "#"
print(my_sign.join(my_tup))

my_lst = ["akhil", 28, True]
mysign = "@"
try:
    print(mysign.join(my_lst))
except:
    print("Obviously throws error as join method takes second arg of sequence types which contains only strings")


# ljust :- The ljust() method will left align the string, using a specified character (space is default) as the fill character.
# length of the string also includes
my_txt = "my name is akhil"
print(my_txt.ljust(20))
print(my_txt.ljust(20,"A"))

# rjust :-  The ljust() method will left align the string, using a specified character (space is default) as the fill character.
# length of the string also includes
print(my_txt.rjust(20))
print(my_txt.rjust(20,"O"))

# rpartition :- The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.
print("akhil#reddy".rpartition("#"))

# rfind :- he rfind() method finds the last occurrence of the specified value.
# The rfind() method returns -1 if the value is not found.
# The rfind() method is almost the same as the rindex() method. See example below.
print(my_txt.rfind("reddy"))
print(my_txt.rfind("akhil"))

#rjust :- The rjust() method will right align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

name = " my name is akhil"
surname = "matta"
print(name.replace("akhil", surname))

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)

# rstrip
# strips the string present in it
# if it is not there it doesnt throw any error

print(my_txt.rstrip("akhil"))
print(my_txt.rstrip("reddy"))

#split :- this method converts the string into list
# based on some value we can split
print(my_txt.split())
name = "akhil"
print(name.split())
name = "akhil#reddy#matta"
print(name.split("#"))

# strip
# The strip() method removes any leading, and trailing whitespaces.
# Leading means at the beginning of the string, trailing means at the end.
# You can specify which character(s) to remove, if not, any whitespaces will be removed.

name = "     akhil"
print(name.strip())
txt = "     banana     "
print(txt.strip())
print("akhila".strip("a"))

# swapcase
# Swaps cases, lower case becomes upper case and vice versa

print("akhil".swapcase())
print("AKHIL".swapcase())

#startswith
# The startswith() method returns True if the string starts with the specified value, otherwise False.
print("akhil is good boy".startswith("akhil"))

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)

# title :- Converts the first character of each word to upper case
print("akhil".title())
print("my name is akhil".title())


"""he translate() method returns a string where some specified characters are replaced with the character described 
    in a dictionary, or in a mapping table.

Use the maketrans() method to create a mapping table.

If a character is not specified in the dictionary/table, the character will not be replaced.

If you use a dictionary, you must use ascii codes instead of characters."""
mydict = {83:  80} #use a dictionary with ascii codes to replace 83 (S) with 80 (P):
txt = "Hello Sam!"
print(txt.translate(mydict))

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

# zfill :- The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
# If the value of the len parameter is less than the length of the string, no filling is done.
txt = "50"

x = txt.zfill(10)

print(x)






