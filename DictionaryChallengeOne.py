# Challenge

# modify the program so that the exits are a dictionary instead of a list
# with the keys being the numbers of the locations and the values being
# dictionaries holding the exits (as they present). No change should be
# needed to the actual code
#
# Once that is working, create another dictionary that contains words that
# players may use. These words will be keys, and their values will be
# a single letter that the program can use to determine which way to go

locations = {0: "you are sitting in from of a computer learning python",
             1: "you are standing at the end of a road before a small brick building",
             2: "you are at the top of a hill",
             3: "you are inside a building, a well house for a small stream",
             4: "you are in a valley beside a stream",
             5: "you are in a forest"}

exits = {0: {"Q": 0},  # Quit
         1: {"W": 2, "E": 3, "S": 4, "N": 5, "Q": 0},  # all cardinal directions
         2: {"N": 5, "Q": 0},  # only north
         3: {"W": 1, "Q": 0},  # only west
         4: {"N": 1, "W": 2, "Q": 0},  # north or west
         5: {"W": 2, "S": 1, "Q": 0}}  # south or west

Directions = {"Quit": "Q", "quit": "Q",  # Quit options
              "North": "N", "north": "N",  # North options
              "East": "E", "east": "E",  # East options
              "South": "S", "south": "S",  # South options
              "West": "W", "west": "W"}  # West options


loc = 1
while True:
    # prints the avaliable directions player can go in
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    # if Q is entered break out of game
    if loc == 0:
        break

    # set Direction equal to you input
    direction = input("Avaliable exits are " + "  " + availableExits.upper() + ": ")
    print()

    # checks if input len is greater than 1
    if len(direction) > 1:
        # # checks if direction is in Directions Dict
        # # loop through Directions to find if word exits
        # for word in Directions:
        #     # if word exists set direction to dictionary value
        #     if word in direction:
        #         direction = Directions[word]

        # loops through a split direction input list
        words = direction.split()
        for word in words:
            # if individual word in Directions dict
            if word in Directions:
                # if entry found set direction = value and break
                direction = Directions[word]
                break

    # if direction valid, set loc to when you are going
    if direction in exits[loc]:
        # loc set to loc (0-4) and what that represents in locations
        loc = exits[loc][direction]

    else:
        # not a valid direction
        print("you cannot go in that direction")

# more efficient code way this Challenge

# # splits all the word of key '0'
# print(locations[0].split())
#
# # splits [3]'s value into a list of before and after ','
# print(locations[3].split(","))
#
# # joins all split words, from locations[0], into a string separated by spaces
# print(' '.join(locations[0].split()))