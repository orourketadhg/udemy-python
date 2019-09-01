#!usr/bin/env python

"""
examining rolling back a database transaction

"""

__author__ = "Tadhg O'Rourke"
__date__ = "01/09/2019"


import sqlite3

db = sqlite3.connect("Accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS Accounts (name TEXT PRIMARY KEY NOT NULL , balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS Transactions (time TIMESTAMP NOT NULL, account TEXT NOT NULL, "
           "amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account(object):

    def __init__(self, name: str, bal: int = 0.0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}".format(self.name))
        else:
            self.name = name
            self._balance = bal
            cursor.execute("INSERT INTO accounts VALUES (?, ?)", (name, bal))
            cursor.connection.commit()
            print("New account {} with €{}".format(self.name, self._balance))

        self.show_balance()

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._balance += amount / 100
            print("deposited €{:.2f}".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount / 100
            print("withdrawn €{:.2f}".format(amount / 100))
            return amount / 100
        else:
            print("must withdraw between 0 and {:.2f}".format(self._balance))

    def show_balance(self):
        print("Balance is currently {:.2f}".format(self._balance))


if __name__ == '__main__':
    john = Account("Tim")
    john.deposit(5230)
    john.show_balance()
    john.withdraw(7480)
    john.show_balance()


