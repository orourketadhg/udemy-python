import tkinter

# # print versions
# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# # Creates a test GUI window
# tkinter._test()

mainWindow = tkinter.Tk()

# adds a title to the GUI window
mainWindow.title("Hello Window")
# sets the window size to 640x480 with 8 pixels in and 400 pixels down
mainWindow.geometry('640x480+8+400')

# adds a label (text box) to the mainWindow screen
label = tkinter.Label(mainWindow, text="hello World")
# location assignment
label.pack(side='top')

# adds a frame to the GUI
leftFrame = tkinter.Frame(mainWindow)

# frame position assignment
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)


# adds a canvas () to the screen, that is raised and has a border of 1
# relief - is the box 3D and is it coming out or going in to the GUI
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)

# Expand must be used if not on its relative side ( top/bottom - Y expand, right/left - X expand)
# # location assignment, will fill the window on Y axis
# canvas.pack(side='left', fill=tkinter.Y)
# # location assignment, will fill the window on X axis
# canvas.pack(side='left', fill=tkinter.X, expand=True)
# # Both X and Y - needs expand
# canvas.pack(side='top', fill=tkinter.BOTH, expand=True)

canvas.pack(side='left', anchor='n')

# right frame creation and position assignment
rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

# buttons are in rightFrame
button1 = tkinter.Button(rightFrame, text="Button1")
button2 = tkinter.Button(rightFrame, text="Button2")
button3 = tkinter.Button(rightFrame, text="Button3")

# creates button
# anchor is relative to previous button
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')


# allows tkinter to take control and open the window
# must be last entry so it can start the window
mainWindow.mainloop()
