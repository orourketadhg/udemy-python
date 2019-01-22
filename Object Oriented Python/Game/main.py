from player import Player
from enemy import Enemy, Troll, Vampyre

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

Dr_Acula = Vampyre("Dr. Acula")
print(Dr_Acula)

# subclass using superclasses methods
troll_1.take_damage(10)
print(troll_1)

# Dr_Acula.take_damage(13)
# print(Dr_Acula)

print("=" * 40)

while Dr_Acula.alive:
    Dr_Acula.take_damage(1)
    print(Dr_Acula)
