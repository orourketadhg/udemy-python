"""
examining the map function

"""

__author__ = "Tadhg O'Rourke"
__date__ = "07/09/2019"

text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)

# use map()
# map(function reference, iterable)
# map() will execute iterate over a iterable preforming a operation that has been referenced - stores result in iterable
map_capitals = list(map(str.upper, text))
print(map_capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

# use map()
map_words = list(map(str.upper, text.split(' ')))
print(map_words)
