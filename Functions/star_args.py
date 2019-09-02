#!usr/bin/env python

"""
Examining star args (*args)

"""

__author__ = "Tadhg O'Rourke"
__date__ = "02/09/2019"


# function takes a variable amount of arguments
def average(*args):

    print(type(args))                       # tuple
    print("args is: {}".format(args))       # print the tuple
    print("*args is: ", *args)              # print the contents of the tuple

    mean = 0
    # unpack the args
    for arg in args:
        mean += arg

    return mean / len(args)


if __name__ == '__main__':

    # the print function has the ability to intake as many arguments as specified (a variable amount of arguments)
    print('hello', 'world')
    print(average(1, 2, 3, 4, 5))
