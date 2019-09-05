#!usr/bin/env python

"""
file descriptor

"""

__author__ = "Tadhg O'Rourke"
__date__ = "05/09/2019"


# generates n odd numbers
# def odd_gen(n: int):
def odd_gen():
    current = 1

    # while current <= n:
    while True:
        yield current
        current += 2


# for i in odd_gen():
#     print(i)


def pi_series():
    odds = odd_gen()
    approx = 0
    while True:

        approx += (4 / next(odds))
        yield approx

        approx -= (4 / next(odds))
        yield approx


approx_pi = pi_series()

for x in range(10000):
    print(next(approx_pi))
