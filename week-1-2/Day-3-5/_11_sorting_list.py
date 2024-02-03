# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
# we can sort strings and numbers as well

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

numlist = [10,9,8,7,6,5]
numlist.sort()
print(numlist)

floatlist = [2.9, 2.8, 2.5, 2.7, 2.3, 2.6]
floatlist.sort()
print(floatlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

numlist = [10,9,8,7,6,5]
numlist.sort(reverse=True)
print(numlist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

"""
Luckily we can use built-in functions as key functions when sorting a list.
So if you want a case-insensitive sort function, use str.lower as a key function:"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

