import random


# class Enemy:
class Enemy(object):

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hp = hit_points
        self._default_hp = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hp - damage

        if remaining_points >= 0:
            self._hp = remaining_points
            print("Enemy took {} points of damage, {} remaining".format(damage, self._hp))
        else:
            self._lives -= 1

            if self._lives > 0:
                print("{0._name}: Lost a life".format(self))
                self._hp = self._default_hp
            else:
                print("{0._name} has died".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, HP: {0._hp}".format(self)


# sub class of Enemy - Troll inherits from Enemy - Inheritance
class Troll(Enemy):

    def __init__(self, name):
        # Python 2 way of doing super class inheritance
        # Enemy.__init__(self, _name=_name, _lives=2, hit_points=15)
        # Python 3 version
        super().__init__(name=name, lives=2, hit_points=15)

    # only a Troll subclass object can use this method
    def grunt(self):
        print("{0._name}: Grunts".format(self))


class Vampyre(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodge(self):
        if random.randint(1, 3) == 3:
            print("{0._name}: Dodged the attack".format(self))
            return True
        else:
            return False

    # method overriding
    def take_damage(self, damage):
        if not self.dodge():
            super().take_damage(damage)


class VampyreKing(Vampyre):

    def __init__(self, name):
        super().__init__(name)
        self._lives = 1
        self._hp = 140

    def take_damage(self, damage):
        super().take_damage(damage // 4)
