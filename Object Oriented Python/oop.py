a = 5
b = 10
print(a + b)
print(a.__add__(b))


# A Class is a template of a piece of code
# creation of a class that prints 'Hello World!'
class ClassName:
    print('Hello World!')


# An Object is a instance of an Class
# creation of a ClassName Object
A = ClassName()


class Kettle(object):

    # initialising passed variables common to all methods in a class
    # self used to access other attributes in a method
    # all other attributes must be initialised in order to be used in the class
    def __init__(self, make, price=100.00):
        # assigning a attribute to self.[name] so it can be used in the class by referring to self.[name]
        self.make = make
        self.price = price
        self.on = False


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

