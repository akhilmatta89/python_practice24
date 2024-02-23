"""
If the value of the variable is not varied from object to object, such type of variables we need to declare within the
class directly but outside of the methods
Such type of methods are called static methods.

For total class only one copy of static variable will be created and shared by all objects of that class.

we can access static variables either by class name or by object reference, but recommended to use class name
"""

class Test:
    x = 10
    def __init__(self):
        self.y = 20

t = Test()
print(t.__dict__)
print("x",t.x, "y",t.y) # Here I  have normal values which are declared
Test.x = 888            # Here iam changing teh x value using class name
print("x",t.x, "y",t.y) # Now you can see the change you made effected to it
t1 = Test()             # Here iam initializing the class again
print("x",t.x, "y",t.y) # Now you can see the change you made effected to the new initialized class as well
t1.x = 999
print("x",t1.x, "y",t.y) # Here i changed using ref variable
print("x",t.x, "y",t.y) # no change the variable stuck to old value itself
# Basically to change static value we need to use class name


# Various places to declare static variables
"""
- Within the class directly but outside of the methods
- inside instance method using class name
- inside constructor using class name
- inside class method using class name or cls variable
- inside static method using class name
"""

class Test1:
    a = 10 # Within the class directly but outside of the methods
    def __init__(self):
        Test1.b = 20 # inside constructor using class name

    def instance_method(self):
        Test1.c = 30 # inside instance method using class name

    @classmethod
    def class_method(cls):
        Test1.d = 40
        cls.e = 50

    @staticmethod
    def static_method():
        Test1.f = 60

print(Test1.__dict__)
t = Test1()
print(Test1.__dict__)
t.instance_method()
print(Test1.__dict__)
Test1.class_method()
print(Test1.__dict__)
Test1.static_method()
print(Test1.__dict__)
Test1.g = 70
print(Test1.__dict__)

# Accessing the static variables
"""
- Inside constructor by using either self or class name.
- Inside Instance method by using either self or class name
- Inside class method using class name or cls variable
- Inside static method using class name
- from outside of the class by using either object reference or class name
"""

class Test2:
    x = 10
    def __init__(self): # Inside constructor by using either self or class name.
        print("iam inside constructor")
        print(self.x)
        print(Test2.x)

    def instance_method(self): # inside instance method using class name
        print("iam inside instance method")
        print(self.x)
        print(Test2.x)

    @classmethod
    def class_method(cls): # Inside class method using class name or cls variable
        print("iam inside class method")
        print(cls.x)
        print(Test2.x)

    @staticmethod
    def static_method(): # Inside static method using class name
        print("iam inside static method")
        print(Test2.x)

t = Test2()
t.instance_method()
t.class_method()
t.static_method()
print("from outside of the class by using either object reference or class name")
print(t.x)
print(Test2.x)

# Modifying the value of the static variable
# Anywhere we can  modify the class variable by using class name
# Inside class method we need to use either with class name or cls variable

class Test3:
    x= 10
    def __init__(self):
        print("Before changing The static variable value is", Test3.x)
        Test3.x = 20
        print("After changing The static variable value is", Test3.x)

t3 = Test3()
print(t3.x)

class Test4:
    x = 10
    def instance_method(self): # Modified using instance method
        Test4.x = 30
t4 = Test4()
t4.instance_method()
print(t4.x)

class Test5:
    x = 10

    @classmethod
    def class_method(cls):
        cls.x = 40
t5 = Test5()
t5.class_method()
print(t5.x)

class Test6:
    x = 10
    @staticmethod
    def static_method():
        Test6.x = 50

t6 = Test6()
t6.static_method()
print(t6.x)

# If we change the static variable by either using self or object reference variable, then the value of the static
# variable won't be changed, just a new instance variable with the same name will be added to the particular object.

class Test7:
    a = 10
    def m1(self):
        self.a = 888

t7 = Test7()
print(t7.a)
t7.m1()
print(t7.a)
print(Test7.a)

# Deleting the static variables (del classname.variablename)
# wen can delete from any where using class name and cls variable from class method

class Test8:
    a = 10
    def m1(self):
        del Test8.a # deleting using teh class name
print("before deleting",Test8().a)
t8 = Test8()
print("after deleting", t8.__dict__)

class Test9:
    a = 20

    @classmethod
    def class_method(cls):
        del cls.a

print("before deleting",Test9().a)
t9 = Test9()
print("after deleting", t9.__dict__)

class Test10:
    a = 30

    @staticmethod
    def static_method():
        del Test10.a

print("before deleting",Test10().a)
t10 = Test10()
print("after deleting", t10.__dict__)

class Test11:
    a = 40

    def m1(self):
        self.b = 20

t11 = Test11()
# del t11.a # we cannot delete this as we can only read static variables we cannot modify or delete it using
# object reference variable


