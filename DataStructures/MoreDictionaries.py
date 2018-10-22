# fruit = {"orange": "a sweet, orange, citrus fruit",
#          "lemon": "a sour, yellow, citrus fruit",
#          "grape": "a small, fruit growing in bunches",
#          "lime": "a sour, green citrus fruit",
#          "apple": "round and crunchy"}
#
# print(fruit)
# print(fruit.items())
#
# # returns a list of (key, value) tuple pairs
# f_tuple = tuple(fruit.items())
#
# print(f_tuple)
#
# for snack in f_tuple:
#     item, description = snack
#     print(item + " is " + description)
#
# print(dict(f_tuple))

locations = {0: "you are sitting in from of a computer learning python",
             1: "you are standing at the end of a road before a small brick building",
             2: "you are at the top of a hill",
             3: "you are inside a building, a well house for a small stream",
             4: "you are in a valley beside a stream",
             5: "you are in a forest"}

exits = [{"Q": 0},  # Quit
         {"W": 2, "E": 3, "S": 4, "N": 5, "Q": 0},  # all cardinal directions
         {"N": 5, "Q": 0},  # only north
         {"W": 1, "Q": 0},  # only west
         {"N": 1, "W": 2, "Q": 0},  # north or west
         {"W": 2, "S": 1, "Q": 0}]  # south or west

loc = 1
while True:
    # prints the avaliable directions player can go in
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    # if Q is entered break out of game
    if loc == 0:
        break

    # set Direction equal to you input
    direction = input("Avaliable exits are " + "  " + availableExits.upper())
    print()
    # if direction valid, set loc to when you are going
    if direction in exits[loc]:
        # loc set to loc (0-4) and what that represents in locations
        loc = exits[loc][direction]
    else:
        # not a valid direction
        print("you cannot go in that direction")

