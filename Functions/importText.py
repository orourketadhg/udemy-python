# allows for importing of another a python file
# imports and executes the imported functions
from Functions import *

# prints file name without path or extension

# running a python file that has this in it will print its file name
print(__name__)

# incorrect error
# Functions.python_food()

# functions with a '_' at the start of the name are protected and cannot be run outside its python file
# Functions._center_text('test')

g = sorted(globals())

# will not print print functions starting with '_'
for i in g:
    print(i)

# variables that start and end with 2 underscores '_' are thing that should not be changed

# variables that are a throwaway - temp - can be called either '_' or '__'
