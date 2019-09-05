#!usr/bin/env python

"""
file descriptor

"""

__author__ = "Tadhg O'Rourke"
__date__ = "05/09/2019"


# generates n odd numbers
def odd_gen(n: int):
    current = 1
    while current <= n:
        yield current
        current += 2


for i in odd_gen(100):
    print(i)
