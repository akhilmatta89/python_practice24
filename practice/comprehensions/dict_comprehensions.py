"""
Practical Use Cases for Dictionary Comprehensions
    Transforming dictionaries: Modifying values, keys, or both in an existing dictionary.
    Filtering dictionaries: Creating a dictionary with only the key-value pairs that meet certain criteria.
    Building dictionaries from lists: Creating mappings from list elements.
    Inverting dictionaries: Swapping keys and values.
"""

dicts = {x:x**2 for x in range(10)}
print(dicts)

dict_even = {x:x**2 for x in range(10) if x%2==0}
print(dict_even)

original_dict = {"a":1, "b":2, "c":3}
modified_dict = {k : v**2 for k,v in original_dict.items()}
print(modified_dict)

even_or_odd_dict = {k: ("even" if k%2==0 else "odd") for k in range(10)}
print(even_or_odd_dict)