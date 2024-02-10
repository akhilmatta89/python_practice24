# Python has two built-in methods that you can use on tuples.
# The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.

mylst = ("akhil", "reddy", "matta", "akhil")
print(mylst.count("akhil")) # Returns the number of times a specified value occurs in a tuple

mylst = ("akhil", "reddy", "matta", "akhil", "Mykey", "UST")
print(mylst.index("akhil", 1, 4))