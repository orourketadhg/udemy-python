"""
List comprehensions

"""

__author__ = "Tadhg O'Rourke"
__date__ = "06/09/2019"

# prints path
print(__file__)

numbers = (1, 2, 3, 4, 5, 6)

squares = []
for number in numbers:
    squares.append(number ** 2)

print(squares)


