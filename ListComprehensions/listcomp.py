"""
List comprehensions

"""

__author__ = "Tadhg O'Rourke"
__date__ = "06/09/2019"

print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("please enter a number: "))

# list comprehension
# [ expression | iteration ]
# expression is what will be returned - numbers ** 2
# iteration is what will be iterated over - for number in numbers

squares = [number ** 2 for number in numbers]
# squares = [number ** 2 for number in range(1, 7)]   # using a generator

# set comprehension
squares_set = {number ** 2 for number in numbers}

index_pos = numbers.index(number)
print(squares[index_pos])

print(squares)
