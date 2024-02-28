"""
POLYMORPHISM - Many forms
one thing taking multiple forms is called polymorphism
we have different concepts in polymorphism
    - Duck typing
    - overloading
        - operator overloading
        - method overloading
        - constructor overloading
    - overriding
        - method overriding
        - constructor overriding
"""
print("--------------------------------------------Duck Typing--------------------------------------------------------")
# Duck typing
# in python we cannot specify the type explicitly, based on provided value at the run time the type will be considered
# we cannot decide at the beginning ,if it walks like a duck, quacks like a duck, it must be a duck, python follows this
# principle, this is called duck typing philosophy
class Maruthi:
    def mileage(self):
        print("maruti mileage is 14")

class Tata:
    def mileage(self):
        print("Tata mileage is 18")

class Kia:
    def mileage(self):
        print("Kia mileage is 13")

class Mahindra:
    def cc(self):
        print("cc of mahindra car is 1500 CC")

t = [Maruthi(),Tata(),Kia()]
for i in t:
    i.mileage()

# The problem in above approach is  if the method is not present it throws attribute error for thos we can use hasattr
# method and deal accordingly

t = [Maruthi(),Tata(),Mahindra(), Kia()]
for i in t:
    if hasattr(i, 'mileage'):
        i.mileage()
    if hasattr(i, "cc"):
        i.cc()

print("--------------------------------------------overloading--------------------------------------------------------")
# we can use same operator or methods for different purposes
# eg 1:- 10+20, "akhil"+"reddy"
# eg 2:- 10*20 , "akhil"*2

# There are 3 types of overloading
# - operator overloading
# - method overloading
# - constructor overloading

# opeartor overloading
# we can use same opeartor for multiple purposes which is nothing but oepartor overloading

# example
print(10+20)
print("Akhil"+"Reddy")

# The above method internaslly takes __add__method it would be something like below in the backend
print(int.__add__(10,20)) # if you are trying to add integers
print(str.__add__("akhil","Reddy")) # if str
print(int.__mul__(2,5)) # if you want to perform multiplication
print(int.__sub__(10,20)) # if you want to perform sub
print(int.__gt__(20,10)) # checks greater than
print(int.__pow__(5,5)) # these all come as bultins

# if we want to add 2 classes related methods

class Student:
    def __init__(self, mark_1, mark_2):
        self.mark_1 = mark_1
        self.mark_2 = mark_2

    def __add__(self, other):
        total_marks_1 = self.mark_1 + other.mark_1
        total_marks_2 = self.mark_2 + other.mark_2
        return total_marks_1, total_marks_2


s1 = Student(28, 68)
s2 = Student(29, 69)
# print(s1+s2) # unsupported operand type(s) for +: 'Student' and 'Student'
# if you will not overload the method, we can overload + operator to work with student objects as well by adding __add__
# method with your functionality
print(s1+s2)

# overloading greater than or eq or le ot ge
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __le__(self, other):
        return self.salary <= other.salary

e1 = Employee("akhil",10000)
e2 = Employee("jaya",9000)
print("e1>e2", e1>e2)
print("e1=e2", e1==e2)
print("e2<=e1", e2<=e1)

# Method overloading

# If 2 methods have same name but different type of arguments then those methods are said to be overloaded methods
# Unfortunately python doesnt support method overloading, if you have same method names pythn considersthe last method as valid one

class Test:

    def m1(self):
        print("No Arg")
    def m1(self,a):
        print("One Arg",a)
    def m1(self, a,b):
        print("Two args", a, b)

t = Test()
# t.m1() # m1() missing 2 required positional arguments: 'a' and 'b'
# t.m1(10) # m1() missing 1 required positional argument: 'b'
t.m1(10,20) # This works fine as python considers last method as valid one

# Hnadling method overloding in python
class Test:

    def m1(self, a=None, b=None, c=None):
        if a and b and c:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print("provide atleast 2 args")

# Constructor Overloading

# Constructor overloading is not possibel in python
# if you give mutiple constructors the last one will be taken into effect

class Cars:
    def __init__(self):
        print("first init function")
    def __init__(self):
        print("second init function")
    def __init__(self):
        print("last init function") # This takes effect

Cars()

# Constructor with variable number of args

class Test_2:
    def __init__(self, *a):
        print("the args are", a) # a returns as tuple

Test_2(10,20,30,40)


# Method Overriding
# whatever methods which are avaialable in the parent class are avialbel in the child class aswell defaultly through inheritance
# if the child class is not satisfied with the parent calls implementation then child class can redine as per its functionality
# This concept is called overriding.

class Breeza:
    def cc(self):
        print("The cc of the car is 1500 CC")
    def colors(self):
        print("The colors present are red,black, white")

class GrandVitara(Breeza):
    def colors(self): # here iam overring teh method
        print("The colors present are red, black, white, marroon")

b = Breeza()
b.cc()
b.colors()
g = GrandVitara()
g.cc()
g.colors()

# from overriding the method in child class we can also call parent class method as well
class Breezaa:
    def cc(self):
        print("The cc of the car is 1500 CC")
    def colors(self):
        print("The colors present are red,black, white")

class GrandVitaraa(Breezaa):
    def colors(self): # here iam overring teh method
        super().colors() # here we can call parent class method as well
        print("The colors present are red, black, white, marroon")

b = Breezaa()
b.cc()
b.colors()
g = GrandVitaraa()
g.cc()
g.colors()

# Constructor Overlaoding
class P:
    def __init__(self):
        print("Parent Constructor")
class C(P):
    def __init__(self):
        print("Child Constructor")
class OC(P): # as here we dont have any constructor parent one executes
    def m1(self):
        print("m1 method")
c = C()
p = P()
oc = OC()


# Program to call parent class constructor fron child class
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class B(A):
    def __init__(self,name,age, salary):
        super().__init__(name,age)
        self.salary = salary
        print(self.name,self.age,self.salary)

a = A("akhil",28)
b = B("jaya",28, 20000)



