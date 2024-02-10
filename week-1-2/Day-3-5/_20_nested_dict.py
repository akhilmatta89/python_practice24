employees = {
    "employee_1":{
       "name":"John",
        "DOB":1994
    },
    "employee_2":{
        "name":"dom",
        "DOB":1989
    },
    "employee_3":{
        "name":"jeff",
        "DOB":1990
    }
}
print(employees)

# One more way is
employee1 = {"name":"akhil", "age":28}
employee2 = {"name":"prasanth", "age":26}
employye3 = {"name":"raihan", "age":42}

employees = {
    "employee_1":employee1,
    "employee_2":employee2,
    "employee_3":employye3
}
print(employees)

# Access Items in Nested Dictionaries
print(employees["employee_1"]["name"])

