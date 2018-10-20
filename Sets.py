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
Set2 = evenByTwo - evenByFive
print(sorted(Set1))
print(sorted(Set2))

# update difference
# updates an already existing set by set subtraction
# evenByTwo.difference_update(evenByFive)

# symmetric sets
# will return a set of values that are not common to both sets (i.e only values that are not in both)
print(evenByTwo.symmetric_difference(evenByFive))

# update symmetric set
# will update an already existing set by removing common values
# evenByTwo.symmetric_difference_update(evenByFive)

# isdisjoint
# returns True/False on if the sets have any over lap (i.e checks to see if there are any common values)
print(evenByTwo.isdisjoint(evenByFive))

# add and remove a value from a set
evenByFive.add(100)
# two ways to remove a value
evenByFive.remove(0)  # must be in the set or will return an error
evenByFive.discard(35)

print(sorted(evenByFive))

# issuperset
# returns True/False if a set contains all values of another set
set10 = {1, 2, 3, 4, 5}
set11 = {1, 3, 5}

print(set10.issuperset(set11))

# frozen set
# a set that cannot be changed once created
frozenSet = frozenset(range(0, 10))
