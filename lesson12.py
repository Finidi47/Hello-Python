# Object oriented programming

class Account:
    def __init__(self, full_name, number, phone, balance):
        self.full_name = full_name  # constructor - special method/function that set up info
        self.number = number
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount
        print(f"Amount ${amount} deposited successfully to account ${self.number}")

    def withdraw(self, amount):

        if self.balance < amount:
            print(f"Insufficient funds. Balanace is ${self.balance}")
        else:
            self.balance -= amount
            print(f"amount ${amount} withdrawn successfully from account ${self.number}")


    def check_balance(self):
        print(f"Balance for account ${self.number} is {self.balance}")


kevo_acc = Account(full_name="Kevin Maina", number="0010", phone="0719266487", balance=1000, )
sara_acc = Account("Sarah Hassan", "00230", "0719266487", 1800, )

kevo_acc.deposit(2000)
kevo_acc.check_balance()
kevo_acc.withdraw(500)
kevo_acc.check_balance()

sara_acc.deposit(1000)
sara_acc.check_balance()
