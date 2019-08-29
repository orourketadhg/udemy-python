#!usr/bin/env python

"""
file descriptor

"""

__author__ = "Tadhg O'Rourke"
__date__ = "29/08/2019"

import sqlite3

# create connection to db
db = sqlite3.connect("contacts.sqlite")

new_email = "Bleep@email.com"
new_phone = input("phone Number: ")

# run update
# update_sql = "UPDATE contacts SET email = '{}' WHERE phone == {}".format(new_email, new_phone)

# to attempt to stop sql injection attacks
update_sql = "UPDATE contacts SET email = ? WHERE phone == ?"
update_cursor = db.cursor()

# will run multiple statements at once - separated by semicolons
# extra parameters will replace the question marks in the sql statement - will parse to stop injection attacks
update_cursor.execute(update_sql, (new_email, new_phone))

# commit update
update_cursor.connection.commit()

update_cursor.close()

# get count of rows affected
print(update_cursor.rowcount)

for row in db.execute("SELECT * FROM Contacts"):
    print(row)


db.close()
