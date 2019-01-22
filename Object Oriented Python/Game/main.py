from player import Player
from enemy import Enemy, Troll

player_1 = Player("Tadhg")

zombie = Enemy("Zombie", 5, 1)
print(zombie)

# zombie.take_damage(4)
# print(zombie)
#
# zombie.take_damage(1)
# print(zombie)
#
# zombie.take_damage(6)
# print(zombie)

troll_1 = Troll("Og", 10, 3)
print(troll_1)

troll_2 = Troll("Bog", 10, 4)
print(troll_2)
