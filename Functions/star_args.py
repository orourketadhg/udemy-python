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


# challenge function
def build_tuple(*args):
    return args

    # temp = []
    # for arg in args:
    #     temp.append(arg)
    # return tuple(temp)


# **kwargs unpacks a dictionary of named arguments - similar to star args but with named parameters
def print_backwards(*args, **kwargs):
    print(type(kwargs))                     # dict

    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)


if __name__ == '__main__':
    message = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")

    # the print function has the ability to intake as many arguments as specified (a variable amount of arguments)
    print('hello', 'world')

    # print(average(1, 2, 3, 4, 5))

    # print(type(message))
    # print(message)

with open ('file.txt', 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards)
