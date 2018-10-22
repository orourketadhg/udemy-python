# dictionaries are accessed by a key not by a ordered location

# dictionary name = {key: value, key: value}
fruit = {"orange": "a sweet, orange, citrus fruit",
         # "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         # lowest on the list will be the one displayed
         "apple": "round and crunchy"}

# print(fruit)
# # how to access the value
# print(fruit["lemon"])
#
# fruit["pear"] = "an odd shaped apple"
# print(fruit["pear"])
# # overwrote "pear"
# fruit["lime"] = "great with tequila"
# print(fruit)
# print(fruit["pear"])
#
# print(fruit["apple"])
#
# # deletes ["lemon"]
# del fruit["lemon"]
# print(fruit)
#
# # will delete the dictionary
# # del fruit
#
# # clears the dictionary leaving an empty one
# # fruit.clear()
# # print(fruit)

# print(fruit["tomato"])

# # will get user to enter a key
# # if key invalid "none" will be printed
# while True:
#     dictKey = input('>>>')
#     if dictKey == 'quit':
#         break
#
#     # # check if key exists
#     # if dictKey in fruit:
#     #     description = fruit[dictKey]
#     #     print(description)
#     # else:
#     #     print("{} does not exit".format(dictKey))
#
#     # alternative way to check if key exists
#     description = fruit.get(dictKey, "we don't have a " + dictKey)
#     print(description)

# will print all values of fruit
# order will change every time
# for snack in fruit:
#     print(snack)

# will print the keys and values in order every time as they are printed from a list
# ordered_key = list(fruit.keys())
# ordered_key.sort()
# for f in ordered_key:
#     print(f + " - " + fruit[f])

# will print the values in fruit
for val in fruit.values():
    print(val)
