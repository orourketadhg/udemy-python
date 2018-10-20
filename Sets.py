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
# print(even)

# Union
evenByFour = set(range(0, 40, 4))

unionTwoFour = evenByTwo.union(evenByFour)
print(unionTwoFour)
