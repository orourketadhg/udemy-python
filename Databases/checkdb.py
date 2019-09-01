#!usr/bin/env python

"""
file descriptor

"""

__author__ = "Tadhg O'Rourke"
__date__ = "01/09/2019"

import sqlite3

db = sqlite3.connect("Accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM localhistory"):
    print(row)

db.close()
