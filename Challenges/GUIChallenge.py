# Challenge

# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import tkinter


mainWindow = tkinter.Tk()

# my attempt

# mainWindow.geometry('512x480')
# mainWindow['padx'] = 16
#
# # mainWindow.columnconfigure(0, weight=1)
# # mainWindow.columnconfigure(1, weight=2)
# # mainWindow.columnconfigure(2, weight=2)
# # mainWindow.columnconfigure(3, weight=2)
# # mainWindow.rowconfigure(0, weight=1)
# # mainWindow.rowconfigure(1, weight=1)
# # mainWindow.rowconfigure(2, weight=1)
# # mainWindow.rowconfigure(3, weight=1)
# # mainWindow.rowconfigure(4, weight=1)
# # mainWindow.rowconfigure(5, weight=1)
#
# # output Window
# outputBox = tkinter.Entry(mainWindow, width=29)
# outputBox.grid(row=0, column=0, sticky='nsew')
#
# # buttons
# buttonFrame = tkinter.Frame(mainWindow)
# buttonFrame.grid(row=1, column=0)
# ButtonList = ('C', 'CE', '7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '0', '=', '/')
#
# i = 0
#
# # row 1
# cButton = tkinter.Button(buttonFrame, text=ButtonList[0], width=6)
# ceButton = tkinter.Button(buttonFrame, text=ButtonList[1], width=6)
# cButton.grid(row=1, column=0, sticky='w')
# ceButton.grid(row=1, column=1, sticky='w')
#
# # row 2
# sevenButton = tkinter.Button(buttonFrame, text=ButtonList[2], width=6)
# eightButton = tkinter.Button(buttonFrame, text=ButtonList[3], width=6)
# nineButton = tkinter.Button(buttonFrame, text=ButtonList[4], width=6)
# plusButton = tkinter.Button(buttonFrame, text=ButtonList[5], width=6)
# sevenButton.grid(row=2, column=0, sticky='w')
# eightButton.grid(row=2, column=1, sticky='w')
# nineButton.grid(row=2, column=2, sticky='w')
# plusButton.grid(row=2, column=3, sticky='w')
#
# # row 3
# fourButton = tkinter.Button(buttonFrame, text=ButtonList[6], width=6)
# fiveButton = tkinter.Button(buttonFrame, text=ButtonList[7], width=6)
# sixButton = tkinter.Button(buttonFrame, text=ButtonList[8], width=6)
# minusButton = tkinter.Button(buttonFrame, text=ButtonList[9], width=6)
# fourButton.grid(row=3, column=0, sticky='w')
# fiveButton.grid(row=3, column=1, sticky='w')
# sixButton.grid(row=3, column=2, sticky='w')
# minusButton.grid(row=3, column=3, sticky='w')
#
# # row 4
# oneButton = tkinter.Button(buttonFrame, text=ButtonList[10], width=6)
# twoButton = tkinter.Button(buttonFrame, text=ButtonList[11], width=6)
# threeButton = tkinter.Button(buttonFrame, text=ButtonList[12], width=6)
# multButton = tkinter.Button(buttonFrame, text=ButtonList[13], width=6)
# oneButton.grid(row=4, column=0, sticky='w')
# twoButton.grid(row=4, column=1, sticky='w')
# threeButton.grid(row=4, column=2, sticky='w')
# multButton.grid(row=4, column=3, sticky='w')
#
# # row 5
# zeroButton = tkinter.Button(buttonFrame, text=ButtonList[14], width=6)
# equalButton = tkinter.Button(buttonFrame, text=ButtonList[15], width=13)
# divideButton = tkinter.Button(buttonFrame, text=ButtonList[16], width=6)
# zeroButton.grid(row=5, column=0)
# equalButton.grid(row=5, column=1, columnspan=2)
# divideButton.grid(row=5, column=3)
#

# masterClass version

# list of lists
keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)]]

mainWindowPadding = 8

mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = mainWindowPadding

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

keypad = tkinter.Frame(mainWindow)
keypad.grid(row=1, column=0, sticky='nsew')

# for loop to add buttons
row = 0
# row loop
for keyRow in keys:
    col = 0
    # col loop
    for key in keyRow:
        # creates new button
        #  sticky=tkinter.E + tkinter.W - fills the width of its cell
        tkinter.Button(keypad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1


mainWindow.update()
# sets the smallest to be(keypad frame width + 8)(the keypad frame height + result frame)
mainWindow.minsize(keypad.winfo_width() + mainWindowPadding, result.winfo_height() + keypad.winfo_height())
# having both mix and max makes it so it can only be one size
mainWindow.maxsize(keypad.winfo_width() + mainWindowPadding + 50, result.winfo_height() + keypad.winfo_height() + 50)

mainWindow.mainloop()


