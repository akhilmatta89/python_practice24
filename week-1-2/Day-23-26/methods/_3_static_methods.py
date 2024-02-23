"""
In general these methods are utility methods
Inside these methods we dont use any instance or class level variables
here we wont provide cls or self variables at the time of declaration

we can declare static method expliccitly by using @staticmethod decorator
we can access static methods by using class name or object reference
"""

class AirthematicOperations:

    @staticmethod
    def addition(x, y):
        return x + y

    @staticmethod
    def subtraction(x, y):
        return x - y

    @staticmethod
    def multiplication(x,y):
        return x * y

a = AirthematicOperations()
print(a.addition(2, 5))
print(AirthematicOperations.subtraction(2,2))
