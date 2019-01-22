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

# instantiating a subclass method
troll_1 = Troll("Og")
print(troll_1)

troll_2 = Enemy("Bog", 10, 1)
print(troll_2)

# using a subclasses methods
troll_1.grunt()

# as troll 2 is not a Troll object it cannot use the sub classes methods
# troll_2.grunts()
