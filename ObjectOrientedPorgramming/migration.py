#!usr/bin/env python

"""
file descriptor

"""

__author__ = "Tadhg O'Rourke"
__date__ = "30/08/2019"

import ObjectOrientedPorgramming.ducks as ducks

flock = ducks.Flock()
duck1 = ducks.Duck()
duck2 = ducks.Duck()
duck3 = ducks.Duck()
duck4 = ducks.Duck()
duck5 = ducks.Duck()
duck6 = ducks.Duck()
duck7 = ducks.Duck()
penguin = ducks.Penguin()

flock.add_duck(duck1)
flock.add_duck(duck2)
flock.add_duck(duck3)
# will not be added to flock as no fly method exists in penguin class
# flock.add_duck(penguin)
flock.add_duck(duck4)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

flock.migrate()
