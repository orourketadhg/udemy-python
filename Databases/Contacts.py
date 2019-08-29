#!usr/bin/env python

"""
Basics of sqlite in python

"""

__author__ = "Tadhg O'Rourke"
__date__ = "29/08/2019"

import sqlite3

# create connection to db
db = sqlite3.connect("contacts.sqlite")

# execute db commands

# creates table if it doest already exist
db.execute("CREATE TABLE IF NOT EXISTS Contacts (name TEXT, phone INTEGER, email TEXT)")

# insert data into table
db.execute("INSERT INTO Contacts (name, phone, email) VALUES ('Test', 123456789, 'test@email.com')")
db.execute("INSERT INTO Contacts VALUES ('Test1', 123456788, 'test1@email.com')")

# get data from db
cursor = db.cursor()
cursor.execute("SELECT * From contacts")

# for row in cursor:
#     print(row)

# returns all rows in a list
# print(cursor.fetchall())

# returns the next row
print(cursor.fetchone())

# will run from the cursors current position
for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("*" * 20)

# will not execute as cursor at enc of statement - need to execute statement again
# for name, phone, email in cursor:
#     print(name)
#     print(phone)
#     print(email)
#     print("*" * 20)

# close the cursor
cursor.close()

# commit changes to db
db.commit()

# close db
db.close()
