class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Flying easily")
        elif self.ratio == 1:
            print("Struggling to fly")
        else:
            print("Unable to fly")


class Duck(object):

    def __init__(self):
        # creating a class object in a class
        self._wing = Wing(1.8)

    def walk(self):
        print("duck: waddle")

    def swim(self):
        print("duck: Swim")

    def quack(self):
        print("duck: Quack")

    # Example of composition
    def fly(self):
        # using a class objects methods
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("penguin: waddle")

    def swim(self):
        print("penguin: Swim")

    def quack(self):
        print("penguin: I don't quack")


# demonstrating raising exceptions
class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck):
        self.flock.append(duck)

    def migrate(self):
        for duck in self.flock:
            duck.fly()


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == "__main__":
    donald = Duck()
    donald.fly()

    # # apparently python thinks billy is a duck
    # billy = Penguin()
    # test_duck(billy)
