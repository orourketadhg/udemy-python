"""
list comprehension examples

"""

__author__ = "Tadhg O'Rourke"
__date__ = "06/09/2019"

text = "what have the romans ever done for us"

# using a list comprehensions

capitals = [char.upper() for char in text]
print(capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

# dont use list comprehensions unnecessarily - can be less efficient
lc_words = text.upper().split(' ')
print(lc_words)
