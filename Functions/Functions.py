# creates function that require no parameters
def python_food():
    width = 80
    text = 'Spam and eggs'
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# parameters data type does matter
# expects a string
# *[name] allows for multiple parameters to be past to a function
# [name]='' - sets a default for a argument if not defined when passing as a parameter
def center_txt(*args, sep=' ', end='\n', file=None, flush=False):
    # will cast to a string
    # text = str(text)
    text = ''
    # handles the multiple arguments that would be passed as parameters
    for arg in args:
        text += str(arg) + sep

    left_margin = (80 - len(text)) // 2
    # Note: end=,file=,flush= are part of print() while the data being assigned are the defaults from this function
    print(" " * left_margin, text, end=end, file=file, flush=flush)


# call function
python_food()

# pass an arguments
center_txt('Eggs and spam')
center_txt('This is a test message')
# center_txt(str(8))

# sends a single string
center_txt("one, two, 3, 4, five")
# sends multiple parameters
center_txt("one", "two", 3, 4, "five", sep=';')


