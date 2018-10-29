import tkinter
import os

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 8

label = tkinter.Label(mainWindow, text="TKinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

# set row and column weights
# weight alters the relationship/location if altering window size
# low weight if widgets are above/below so they stay in a good place
# listbox only real benefit of having a high weight
# horizontal weights will affect scroll bar -- give it a very low weight relative
mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)
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



# Result Box
resultLabel = tkinter.Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')

# Text Entry Box
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')



# Time Spinner
# Frame
timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='nsw')

# Time spinner options
# values/(from_ to) are the numbers able to be chosen in the spinners
# value will always take add -1 to the value
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)

# Time spinner locations
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)

# adds padding on x axis
timeFrame['padx'] = 36



# Date Spinners
# Frame
dateFrame = tkinter.LabelFrame(mainWindow, text='Date')
dateFrame.grid(row=4, column=0, sticky='nsew')

# Spinners
daySpinner = tkinter.Spinbox(dateFrame, width=2, from_=0, to=31)
monthSpinner = tkinter.Spinbox(dateFrame, width=5, values=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
yearSpinner = tkinter.Spinbox(dateFrame, width=4, from_=0, to=9999)

# Date spinner locations
tkinter.Label(dateFrame, text='Day:').grid(row=0, column=0)
daySpinner.grid(row=0, column=1)
tkinter.Label(dateFrame, text='Month:').grid(row=0, column=2)
monthSpinner.grid(row=0, column=3)
tkinter.Label(dateFrame, text='Year:').grid(row=0, column=4)
yearSpinner.grid(row=0, column=5)

dateFrame['padx'] = 25



# Buttons
okButton = tkinter.Button(mainWindow, text='ok')
# command preforms an action - quit in this case, destroy is a better option
cancelButton = tkinter.Button(mainWindow, text='cancel', command=mainWindow.quit)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')


mainWindow.mainloop()

# prints the radio button value in console
print(rbValue.get())
