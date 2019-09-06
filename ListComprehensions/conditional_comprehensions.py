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
        meals.append("a meal")
print(meals)

# conditional comprehension
# [expression | iterator | filter ]
# filter will filter what will be returned to the variable - cannot have a else like above

# do the same thing - choose which is more readable for filter
# meals = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]
# meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]


# conditional comprehension using a conditional expression
# like a conditional comprehension - allows for more complexity

# [ conditional expression | iterator ]
meals = [meal if "spam" not in meal else "a meal" for meal in menu]
print(meals)

print("=" * 40)

x = 12

# conditional expression - conditional on a single line
expression = "Twelve" if x == 12 else "unknown"

print(expression)
print("=" * 40)

for meal in menu:
    # complex conditional expression - unclear and contains bugs
    print(meal, "contains sausage" if "sausage" in meal else "contains bacon" if "bacon" in meal else "contains egg")

print("=" * 40)


items = set()
for meal in menu:
    for item in meal:
        items.add(item)
print(items)

print("=" * 40)

for meal in menu:
    for item in meal:
        if item in meal:
            print("{} contains {}".format(meal, item))
            break

print("=" * 40)

for x in range(1, 31):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)
