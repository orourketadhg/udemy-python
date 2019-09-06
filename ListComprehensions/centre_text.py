"""
file descriptor

"""

__author__ = "Tadhg O'Rourke"
__date__ = "06/09/2019"


def centre_text(*args):
    # text = ""
    # for arg in args:
    #     text += str(arg) + "-"

    text = "-".join([str(arg) for arg in args])

    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


centre_text('spam and eggs')
centre_text('spam, spam and eggs')
centre_text('12')
centre_text('spam, spam, spam and spam')
centre_text("fist", "second", 3, 4, "fifth")

