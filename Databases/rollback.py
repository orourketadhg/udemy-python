#!usr/bin/env python

"""
examining rolling back a database transaction

"""

__author__ = "Tadhg O'Rourke"
__date__ = "01/09/2019"


class Account(object):

    def __init__(self, name: str, bal: int = 0.0):
        self.name = name
        self._balance = bal
        print("New account {} with €{}".format(self.name, self._balance))

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._balance += amount
            print("deposited €{:.2f}".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print("withdrawn €{:.2f}".format(amount / 100))
            return amount / 100
        else:
            print("must withdraw between 0 and {:.2f}".format(self._balance))

    def show_balance(self):
        print("Balance is currently {:.2f}".format(self._balance))


if __name__ == '__main__':
    john = Account("John", 10000)
    john.show_balance()
    john.deposit(5230)
    john.show_balance()
    john.withdraw(7480)
    john.show_balance()
