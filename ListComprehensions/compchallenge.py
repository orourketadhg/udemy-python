"""
file descriptor

"""

__author__ = "Tadhg O'Rourke"
__date__ = "06/09/2019"


def fizzbuxx(x):
    return "fizzbuzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)


comp = [fizzbuxx(x) for x in range(1, 31)]
print(comp)
