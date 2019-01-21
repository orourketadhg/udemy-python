class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    # getter method
    def get_name(self):
        return self.name

    def _get_lives(self):
        return self._lives

    # setter method
    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negatives")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level >= 1:
            self._level = level
            self._score = (level * 1000) - 1000

        else:
            print("level cannot be less than 1")
            self._level = 1

    # a property allows for the use for hidden getter and setter methods
    # that manipulates a specific 'hidden' class attribute
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    # a default method to print information, when an object is printed
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0._score}".format(self)
