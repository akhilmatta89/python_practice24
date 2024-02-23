# Instance variables
# If the value of the variable is varied from object to object then such type of variables are called instance variables
# For every object a separate copy of instance variables will be created

class Car:
    def __init__(self, model, color):
        self.model = model  # instance variable
        self.color = color  # instance variable


car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")
print(car2.__dict__)  # this returns the dictionary of the particular object


# Where we can declare instance variables
# inside the constructor by using self
# inside a method in the class by using self
# outside the class by using object reference variable

# inside constructor example

class Suzuki:
    def __init__(self):
        self.model = "breeza"  # here we are declaring instance variable inside constructor using self
        self.year = 2022


print(Suzuki().__dict__)


class Hyundai:
    def __init__(self):
        self.model = "i20"
        self.year = 2022

    def variants(self):
        self.top_end = "Asta"  # here iam declaring a instance variable inside a method using self


h = Hyundai()
h.variants()
print(h.__dict__)


class Tata:
    def __init__(self):
        self.model = "nexon"
        self.year = 2022

    def variants(self):
        self.top_end = "Fearless Plus"


t = Tata()
t.variants()
t.base_model = "Smart"  # here iam declaring the instance variable using the object reference variable
print(t.__dict__)

# Accessing the instance variables
# we can access the instance variable by using the self inside the class and by using the object reference outside the
# class

class Kia:
    def __init__(self):
        self.model = "Seltos"
        self.year = 2022

    def variants(self):
        self.top_end = "X-Line"
        self.base_model = "HTE"
        print("iam inside the method: ", self.__dict__)

k = Kia()
k.variants()
print("Iam accessing you outside of the method using ref variable: ", k.base_model)

# Deleting the instance variable
# within the class we can delete and also outside the class we can delete

class Renault:
    def __init__(self):
        self.model = "Kwid"
        self.year = 2022

    def variants(self):
        self.top_end = "Climber"
        self.base_model = "RXE"

    def delete_base_model(self):
        del self.base_model # deleting the instance variable inside the method

r = Renault()
r.variants()
print(r.__dict__)
r.delete_base_model()
print(r.__dict__)
del r.top_end # deleting the instance variable outside the class using ref variable
print(r.__dict__)

r1 = Renault()
r1.variants()
print(r1.__dict__) # Note : the variable which are deleted or modified in one object will not reflect in other object



