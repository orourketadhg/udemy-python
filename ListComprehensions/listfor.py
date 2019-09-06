"""
List comprehensions

"""

__author__ = "Tadhg O'Rourke"
__date__ = "06/09/2019"

# prints path
print(__file__)

numbers = (1, 2, 3, 4, 5, 6)

number = int(input("please enter a number: "))

squares = []
for number in numbers:
    squares.append(number ** 2)

index_pos = numbers.index(number)
print(squares[index_pos])

# print(squares)


