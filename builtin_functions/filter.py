"""
examining the filter function

"""

__author__ = "Tadhg O'Rourke"
__date__ = "07/09/2019"


def not_spam(meal_list: list):
    return "spam" not in meal_list


menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

for meal in menu:
    if "spam" not in meal:
        print(meal)

print("=" * 40)

meals = [meal for meal in menu if "spam" not in meal]
print(meals)

print("=" * 40)

# use filter()
# filter(function reference, iterable)
# filter iterates over an iterable executing a reference to a function that will return true if the condition is met
# stores result in iterable
spamless_meals = list(filter(not_spam, menu))
print(spamless_meals)
