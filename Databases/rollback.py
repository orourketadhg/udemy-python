#!usr/bin/env python

"""
examining rolling back a database transaction

"""

__author__ = "Tadhg O'Rourke"
__date__ = "01/09/2019"

import sqlite3
import datetime
import pytz


db = sqlite3.connect("Accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS Accounts (name TEXT PRIMARY KEY NOT NULL , balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS History (time TIMESTAMP NOT NULL, account TEXT NOT NULL, "
           "amount INTEGER NOT NULL, PRIMARY KEY (time, account))")

db.execute("CREATE VIEW IF NOT EXISTS localhistory AS SELECT strftime('%Y-%m-%d %H:%M:%f', History.time, 'localtime') "
           "AS localtime, History.account ,History.amount FROM History ORDER BY History.time")


class Account(object):

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())
        # local_time = pytz.utc.localize(datetime.datetime.utcnow())
        # return local_time.astimezone()

    def __init__(self, name: str, bal: int = 0.0):
        cursor = db.execute("SELECT name, balance FROM Accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}".format(self.name))
        else:
            self.name = name
            self._balance = bal
            cursor.execute("INSERT INTO Accounts VALUES (?, ?)", (name, bal))
            cursor.connection.commit()
            print("New account {} with €{}".format(self.name, self._balance))

        self.show_balance()

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            # self._balance += amount / 100

            new_balance = self._balance + amount

            # update tables
            self._save_update(new_balance)

            print("deposited €{:.2f}".format(amount))
        return self._balance

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            # self._balance -= amount / 100

            new_balance = self._balance - amount

            # update tables
            self._save_update(new_balance)

            print("withdrawn €{:.2f}".format(amount))
            return amount
        else:
            print("must withdraw between 0 and €{:.2f}".format(self._balance))

    def show_balance(self):
        print("Balance is currently €{:.2f}".format(self._balance))

    # refactored to its own method as common between both deposit and withdraw
    def _save_update(self, amount):
        deposit_time = self._current_time()

        # update database tables
        db.execute("UPDATE Accounts SET balance = ? where (name = ?)", (amount, self.name))
        db.execute("INSERT INTO History VALUES (?, ?, ?)", (deposit_time, self.name, amount))

        # commit changes
        db.commit()

        # update class attribute
        self._balance = amount


if __name__ == '__main__':
    Tim = Account("Tim")
    Tim.deposit(1000)
    Tim.deposit(50)
    Tim.deposit(200)
    Tim.show_balance()
    Tim.withdraw(750)
    Tim.show_balance()

    db.close()
