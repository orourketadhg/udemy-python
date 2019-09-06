"""
file descriptor

"""

__author__ = "Tadhg O'Rourke"
__date__ = "06/09/2019"

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

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("meal skipped")
print(meals)

# conditional comprehension
# [expression | iterator | filter ]
# filter will filter what will be returned to the variable - cannot have a else like above

# do the same thing - choose which is more readable for filter
# meals = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]
meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]

print(meals)
