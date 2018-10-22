import shelve

# pythons standard library
# prints the list of python internal working modules/other stuff
print(dir())

# noinspection PyUnresolvedReferences
# prints list of python's standard functions and functionality
print(dir(__builtins__))

# prints the functions of shelve module
print(dir(shelve))
# will print a list of functions in a class in a module
print(dir(shelve.Shelf))

# will print the documentation of a function
help(dir())
