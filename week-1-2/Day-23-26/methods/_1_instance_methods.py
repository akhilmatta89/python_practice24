"""
inside method implementation if we are using instance variable then such type of methods are called instance methods
inside instant method we need to pass self variable.
By adding self method we can be able to access instance variables
within the class we can access methods using self and outside method we can access using object reference
"""


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Hi, {}".format(self.name))
        print("Your marks are {}".format(self.marks))

    def grade(self):
        if self.marks > 80:
            print("{} passed with first class".format(self.name))
        elif self.marks > 50 and self.marks <= 80:
            print("{} passed with second class".format(self.name))
        elif self.marks > 30 and self.marks <= 50:
            print("{} passed with third class".format(self.name))
        else:
            print("Failed")


n = int(input("enter the number of students you have"))
for i in range(n):
    name = input("enter the name of the student\n")
    marks = int(input("Enter the marks\n"))
    s = Student(name, marks)
    s.display()
    s.grade()
    print("-------------------------------------------------------")

# setter and getter methods
# we can set and get values of the instance variables by using setter and getter methods

# setter methods
# This is used to set values to the instance variables, also called as mutator methods

class Employee:

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

n = int(input("enter the number of employees you have"))
for i in range(n):
    e = Employee()
    name = input("enter the name of the employee\n")
    e.setName(name)
    salary = int(input("Enter the salary\n"))
    e.setSalary(salary)
    print("Hi ", e.getName())
    print("Your salary is", e.getSalary())
    print("-------------------------------------------------------")