# Decorator is used to to modify/beautify a function with additional logics
# Decorator is a function which takes function as the input
# and returns a new function that modfies the existing function
from flask import request


def greet(func):
    def newfunc():
        print("Good Morning Folk!")
        func()
        print("Thanks for usingn this function")
    return newfunc

@greet
def hello():
    print("Hello World!")
"""---------------------------------------------------------------------------------------------"""
def retry(func):
    def my_new_func():
        print("entered into decorator")
        try:
            func()
        except RetryException:
            print("iam saving the failed data into the DB")
    return my_new_func


@retry
def make_an_api_call():
    print("iam trying to make a API call")
    raise RetryException("some error occured")


class RetryException(Exception):
     def __init__(self, message):
         self.message = message
         super().__init__(self.message)



# hello()
make_an_api_call()
