a = 5
b = 10
print(a + b)
# everything in python is an object
# a.__add__(b) is a method for a that adds b to a.
print(a.__add__(b))


# A Class is a template of a piece of code
# creation of a class that prints 'Hello World!'
class ClassName:
    print('Hello World!')


# An Object is a instance of an Class
# creation of a ClassName Object
A = ClassName()


class Kettle(object):

    # init/the constructor class is a automatic method which will declare specified variables when a object is created
    # initialising passed variables common to all methods in a class
    # all other attributes must be initialised in order to be used in the class
    def __init__(self, make, price=100.00):
        # self used to access other attributes in a method
        # assigning a attribute to self.[name] so it can be used in the class by referring to self.[name]
        self.make = make
        self.price = price
        self.on = False

    # creating a method
    def switch_on(self):
        self.on = True


Kenwood = Kettle("Kenwood", 120.00)
hamilton = Kettle("Hamilton")
# . notation is used to access things in a object
print(Kenwood.price)
print(Kenwood.make)

# overwrites object variable price
Kenwood.price = 119.99
print(Kenwood.price)

# can format the replacement fields to hold the class .attribute data
print('Models: {0.make}: {0.price}, {1.make}: {1.price}'.format(Kenwood, hamilton))

"""
Class : template of an object
Object : Instance of a class
Instantiate : Create instance of a class
Method : A function inside a class
Attribute : a variable found in an instance of a class
"""

print(hamilton.on)
# calling the objects method will affect the object variables - in this case
hamilton.switch_on()
print(hamilton.on)

# will create a data attribute only bound to a specific object
hamilton.power = 1.5
print(hamilton.power)
