"""
examining named tuples

"""

__author__ = "Tadhg O'Rourke"
__date__ = "07/09/2019"

from builtin_functions.data import basic_plants_list, plants_list

# a named tuple is named (an instance of a namedtuple() class)and has the elements named - like column names
print(plants_list[0])

# can specify the named element to return
for plant in plants_list:
    print(plant.name)

print()

example = plants_list[0]
print(example)

# replaces the value
example = example._replace(lifecycle='annual')
print(example)

