"""
You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return value are the keys of the dictionary,
but there are methods to return the values as well.
"""
car_dict = {"brand": "maruthi",
            "model": "breeza",
            "electric": False,
            "colors": ["red", "black", "white"],
            "year": 2022,
            "cc": 1497.82}

for i in car_dict: # This for loop returns all keys of the dict
    print(i)
print("----------------")
for i in car_dict: # This for loop returns all values of the dict
    print(car_dict[i])
print("----------------")

# values()
# You can also use the values() method to return values of a dictionary:
for i in car_dict.values():
    print(i)
print("----------------")
# keys()
# You can use the keys() method to return the keys of a dictionary:
for i in car_dict.keys():
    print(i)
print("----------------")

# Loop through both keys and values, by using the items() method:
for key, value in car_dict.items():
    print(key, value)