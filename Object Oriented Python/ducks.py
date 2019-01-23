class Duck(object):

    def walk(self):
        print("duck: waddle")

    def swim(self):
        print("duck: Swim")

    def quack(self):
        print("duck: Quack")


class Penguin(object):

    def walk(self):
        print("penguin: waddle")

    def swim(self):
        print("penguin: Swim")

    def quack(self):
        print("penguin: I don't quack")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == "__main__":
    donald = Duck()
    test_duck(donald)

    # apparently python thinks billy is a duck
    billy = Penguin()
    test_duck(billy)
