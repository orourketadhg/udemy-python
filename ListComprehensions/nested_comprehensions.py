"""
file descriptor

"""

__author__ = "Tadhg O'Rourke"
__date__ = "07/09/2019"

burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "bacon", "tomato"]

# nested iteration in a list comprehension - works like nested for loops

#  [expression | iterator | iterator ] - not technically a list comprehension
# meals = [(burger, topping) for burger in burgers for topping in toppings]
# print(meals)

# iterating through the list comprehension
for meals in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meals)

print()
# the equivalent in a nested for loop

# meals = []
# for burger in burgers:
#     for topping in toppings:
#         meals.append((burger, topping))

# using a list comprehension as the expression in a list comprehension
# [ [ expression | iterator ] | iterator ]
# nested list containing a list of tuples
for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meals)
print()

# swapping order of above
for nested_meals in [[(burger, topping) for topping in toppings] for burger in burgers ]:
    print(nested_meals)
print()
