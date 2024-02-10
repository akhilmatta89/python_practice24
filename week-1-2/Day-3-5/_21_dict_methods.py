car_dict = {"brand": "maruthi",
            "model": "breeza",
            "year": 2022}
print(car_dict)

# clear method
car_dict.clear() # Removes all the elements from the dictionary
print(car_dict)

# copy method
car_dict = {"brand": "maruthi",
            "model": "breeza",
            "year": 2022}
copied_car_dict = car_dict.copy() # Returns a copy of the dictionary
print(copied_car_dict)

# fromkeys method
# The fromkeys() method returns a dictionary with the specified keys and the specified value.
keys = ("brand", "model", "year")
values = ("maruthi", "breeza", 2022)
my_dict = dict.fromkeys(keys, values)
print(my_dict)

# get
# returns value of specified key
car_dict = {"brand": "maruthi",
            "model": "breeza",
            "year": 2022}
print(car_dict.get("model"))

#items
# Returns a list containing a tuple for each key value pair
print(car_dict.items())

# keys
# Returns a list containing the dictionary's keys
print(car_dict.keys())

# pop
# Removes the element with the specified key
car_dict.pop("year")
print(car_dict)

# popitem()
# Removes the last inserted key-value pair
car_dict.popitem()
print(car_dict)

# setdefault
# The setdefault() method returns the value of the item with the specified key.
#
# If the key does not exist, insert the key, with the specified value,
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

b = car.setdefault("year", 2024)
print(b)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)


# Update
car_dict = {"brand": "maruthi",
            "model": "breeza",
            "year": 2022}
car_dict.update({"color":"white"})
print(car_dict)

# values
print(car_dict.values())


