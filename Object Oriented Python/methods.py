class Account:
    """simple account class with balance"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print('Account created for ' + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.show_balance()
        else:
            print('Must withdraw an ammount between 0 and {}'.format(self.balance()))

    def show_balance(self):
        print("Balance is {}".format(self.balance))


# only will run if method.py is the file being run
if __name__ == "__main__":
    acc1 = Account("Tadhg", 0)
    acc1.show_balance()

    acc1.deposit(100)

    acc1.withdraw(50)

    acc1.withdraw(100)
