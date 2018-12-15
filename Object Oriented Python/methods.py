import datetime
import pytz


class Account:
    """simple account class with balance"""

    # creating a static method - a method that doesnt use self
    @staticmethod
    # leading _ - means a pseudo private class
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print('Account created for ' + self.name)
        # empty list is initialised at object instantiation
        self.transaction_list = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            # using Account._current_time as this is a static class method - no self
            # self would still work, but performance would suffer as program would look for namespace before expanding
            # to allow _'s (underscores)
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print('Must withdraw an amount between 0 and {}'.format(self.balance))

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transactions(self):
        # assigns the first element to date and the second to amount
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "Deposited"
            else:
                tran_type = "Withdrawn"
                amount *= -1

            print('{:6} {} on {} (local time was {})'.format(amount, tran_type, date, date.astimezone()))


# only will run if method.py is the file being run
if __name__ == "__main__":
    acc1 = Account("Tadhg", 0)
    acc1.show_balance()

    acc1.deposit(1000)

    acc1.withdraw(500)

    acc1.withdraw(1000)

    acc1.show_transactions()
