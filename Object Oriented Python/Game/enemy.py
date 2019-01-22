# class Enemy:
class Enemy(object):

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hp = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hp - damage
        if remaining_points >= 0:
            self.hp = remaining_points
            print("Enemy took {} points of damage, {} remaining".format(damage, self.hp))
        else:
            self.lives -= 1

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, HP: {0.hp}".format(self)


# sub class of Enemy - Troll inherits from Enemy - Inheritance
class Troll(Enemy):
    pass
