from player import Player

player_1 = Player("Tadhg")

print(player_1.name)
print(player_1.lives)

player_1.lives -= 1
print(player_1)

player_1.lives -= 1
print(player_1)

player_1.lives -= 1
print(player_1)

player_1.lives -= 1
print(player_1)

# getter version
# print(player_1.get_name())

# setter version
# player_1.set_lives(10)
