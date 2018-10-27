import tkinter
import os

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry('640x480-8-200')

label = tkinter.Label(mainWindow, text="TKinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

# set row and column weights
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)



# create a list box
fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for zone in os.listdir('C:\Windows\System32'):
    # inserts to the END of the list (append) with zone file from system32 dir
    fileList.insert(tkinter.END, zone)

# scroll bars are separate widgets
# needs to be oriented, command to
ListScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
ListScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
# link scroll bar to listbox
fileList['yscrollcommand'] = ListScroll.set



# radio button frame
# label frame allows a caption to be set
radioFrame = tkinter.LabelFrame(mainWindow, text='File Details')
radioFrame.grid(row=1, column=2, sticky='ne')

# create radio buttons - all link to 1 variable so only 1 can be selected at a time
rbValue = tkinter.IntVar()
# sets default option
rbValue.set(1)

# add the buttons, with text and values, linking to a variable
radio1 = tkinter.Radiobutton(radioFrame, text="FileName", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(radioFrame, text="PATH", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(radioFrame, text="TimeStamp", value=3, variable=rbValue)

# radio buttons grid location
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

mainWindow.mainloop()

# prints the radio button value in console
print(rbValue.get())
