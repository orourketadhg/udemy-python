"""
examining lambda's

"""

__author__ = "Tadhg O'Rourke"
__date__ = "07/09/2019"

# a lambda is a small single line function with a single expression

x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 10))


# Lambdas should be used in functions or methods
# more powerful to use lambdas in functions
# set arguments for it to use
def mult(a):
    return lambda b: a * b


# test against those arguments
my_f = mult(5)
print(my_f(3))
