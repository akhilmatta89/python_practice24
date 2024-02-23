import sys


class Customer:
    bank_name = "SBI BANK"
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def add_balance(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def balance_enquiry(self):
        return self.balance

    def withdrawal(self, amount):
        if amount > self.balance:
            raise InsufficientFunds
        remaining_amount = self.balance - amount
        self.balance = remaining_amount
        print("Balance after withdrwal of amount is: ", remaining_amount)
        return self.balance

class InsufficientFunds(Exception):

    def __init__(self, message="Amount is not available in you account"):
        self.message = message
        super().__init__(self.message)

print("Welcome to SBI Bank")
c = Customer("akhil")
while True:
    user_request = int(input("enter the string from given values\n1) Add Balance\n2) Balance Enquiry\n3) Withdrawl\n4) Exit\n"))
    if user_request == 1:
        amount = input("enter the amount to add funds")
        c.add_balance(amount)
    elif user_request == 2:
        balance = c.balance_enquiry()
        print("Balance available: ", balance)
    elif user_request == 3:
        amount = int(input("enter the amount to withdraw funds"))
        remaining_amount = c.withdrawal(amount)
        print("Balance available: ", remaining_amount)
    elif user_request == 4:
        print("Thanks for banking")
        sys.exit()
    else:
        print("Invalid request")







