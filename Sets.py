# # syntax for a set
# farmAnimals = {"sheep", "cow", "chicken"}
# print(farmAnimals)
#
# for animal in farmAnimals:
#     print(animal)
#
# print("=" * 40)
#
# # casting a list to a set
# wildAnimals = set(["lion", "tiger", "zebra", "panther"])
#
# print(wildAnimals)
#
# for animal in wildAnimals:
#     print(animal)
#
# print("=" * 40)
#
# # add a new element to the set
# farmAnimals.add("horse")
# wildAnimals.add("horse")
#
# print(farmAnimals)
# print(wildAnimals)
#
# print('=' * 40)

# to create an empty set
# emptySet = set()

evenByTwo = set(range(0, 40, 2))
print(evenByTwo)

evenByFive = set(range(0, 40, 5))
print(evenByFive)

# Union
# returns a set of all the values in both evenByTwo and evenByFive
unionTwoFour = evenByTwo.union(evenByFive)
print(unionTwoFour)

# Intersection
# returns a set of only values that are in both evenByTwo and evenByFive
intersectionTwoFive = evenByTwo.intersection(evenByFive)
print(intersectionTwoFive)

# returns True/False if a set is a subset
setIsSubset = evenByTwo.issubset(evenByFive)
print(setIsSubset)

# set subtraction
# takes one set from another (i.e removes the common values of one set from another)
# returns a set of values that contain only values not in another set
Set1 = evenByTwo.difference(evenByFive)
print(sorted(Set1))




