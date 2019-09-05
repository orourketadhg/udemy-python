#!usr/bin/env python

"""
demonstrating generators and yield

"""

__author__ = "Tadhg O'Rourke"
__date__ = "03/09/2019"

import sys


# A generator function - a generator is a function that returns an object (iterator) which we can iterate over
# create own version of range()
def my_range(n: int):
    start = 0
    while start < n:
        # yield - like a return statement but will not end a function but instead pause it and continue later
        # will pause at the yield and continue when called again
        yield start

        start += 1


# = not the best idea to assign a generator object to a variable - does not reset automatically if overrode by a variable ====

# big_range = range(5)
# create a link to the generator - does not start the function
big_range = my_range(5)

# will iterate over the generators iterable object
# __next__() iterates over an iterable object - first value
print(big_range.__next__())

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

big_list = []
# the first iteration of the for loop is the first time the generator
for val in big_range:
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))

print(big_range)
print(big_list)
