import random


# class Enemy:
class Enemy(object):

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hp = hit_points
        self.default_hp = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hp - damage

        if remaining_points >= 0:
            self.hp = remaining_points
            print("Enemy took {} points of damage, {} remaining".format(damage, self.hp))
        else:
            self.lives -= 1

            if self.lives > 0:
                print("{0.name}: Lost a life".format(self))
                self.hp = self.default_hp
            else:
                print("{0.name} has died".format(self))
                self.alive = False

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, HP: {0.hp}".format(self)


# sub class of Enemy - Troll inherits from Enemy - Inheritance
class Troll(Enemy):

    def __init__(self, name):
        # Python 2 way of doing super class inheritance
        # Enemy.__init__(self, name=name, lives=2, hit_points=15)
        # Python 3 version
        super().__init__(name=name, lives=2, hit_points=15)

    # only a Troll subclass object can use this method
    def grunt(self):
        print("{0.name}: Grunts".format(self))


class Vampyre(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodge(self):
        if random.randint(1, 3) == 3:
            print("{0.name}: Dodged the attack".format(self))
            return True
        else:
            return False

    # method overriding
    def take_damage(self, damage):
        if not self.dodge():
            super().take_damage(damage)
