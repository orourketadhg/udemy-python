# Note: This code will act different on different versions of Python and on different OS's

import tkinter

# grid is a simpler geometry manager

mainWindow = tkinter.Tk()

mainWindow.title("Hello Window")
mainWindow.geometry('640x480-8-200')

label = tkinter.Label(mainWindow, text="hello World")
# grid method works as a table in relation to other GUI objects
# row for row position, column for column position
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
# sticky works as a lock for relative positions
rightFrame.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(rightFrame, text="Button1")
button2 = tkinter.Button(rightFrame, text="Button2")
button3 = tkinter.Button(rightFrame, text="Button3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
# alternative to columnconfigure
mainWindow.grid_rowconfigure(2, weight=1)

# add attributes to frames
leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
# set grids sticky to specified compass points
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

# widen button2
rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew', )

mainWindow.mainloop()


