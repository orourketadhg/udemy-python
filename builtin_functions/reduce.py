"""
examining the reduce function

"""

__author__ = "Tadhg O'Rourke"
__date__ = "07/09/2019"

import functools


# function to be referenced
def calc_values(x, y: int):
    return x + y


numbers = [2, 3, 5, 8, 13]

# use reduce()
# reduce(function reference, iterable)
# reduce() will the (n)th and (n + 1)th values and preform the function referenced too by them then iterate forward and
# repeat -
reduced_value = functools.reduce(calc_values, numbers)
print(reduced_value)

# what is actually happening
result = calc_values(2, 3)          # 2 + 3 = 5
result = calc_values(result, 5)     # 5 + 5 = 10
result = calc_values(result, 8)     # 10 + 8 = 18
result = calc_values(result, 13)    # 18 + 13 = 31
print(result)
