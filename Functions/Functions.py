# creates function that require no parameters
def python_food():
    width = 80
    text = 'Spam and eggs'
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# parameters data type does matter
# expects a string
def center_txt(text):
    # will cast to a string
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call function
python_food()

# pass an arguments
center_txt('Eggs and spam')
center_txt('This is a test message')
# center_txt(str(8))
