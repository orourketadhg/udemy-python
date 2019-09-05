#!usr/bin/env python

"""
file descriptor

"""

__author__ = "Tadhg O'Rourke"
__date__ = "05/09/2019"


# fibonacci generator
def fibonacci():
    current, previous = 0, 1

    while True:
        # yield next value
        yield current

        # update fibonacci values
        current, previous = current + previous, current


fib = fibonacci()

# next(i) == __next__()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
