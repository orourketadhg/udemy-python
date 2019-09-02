#!usr/bin/env python

"""
file descriptor

"""

__author__ = "Tadhg O'Rourke"
__date__ = "02/09/2019"


import sqlite3
import tkinter

db_connection = sqlite3.connect('music.db')

mainWindow = tkinter.Tk()
mainWindow.title("Music DB Browser")

mainWindow.geometry('1024x768')

#       Configure rows and columns
mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)     # spacer column

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)


#       labels
tkinter.Label(mainWindow, text='Artist').grid(row=0, column=0)
tkinter.Label(mainWindow, text='Album').grid(row=0, column=1)
tkinter.Label(mainWindow, text='Songs').grid(row=0, column=2)


#       Artists Listbox
artist_list = tkinter.Listbox(mainWindow)
artist_list.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artist_list.config(border=2, relief='sunken')

artist_scroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artist_list.yview)
artist_scroll.grid(row=1, column=0, sticky='nse', rowspan=2)
artist_list['yscrollcommand'] = artist_scroll.set

#       Album Listbox
album_lv = tkinter.Variable(mainWindow)
album_lv.set(("Choose an Artist",))
album_list = tkinter.Listbox(mainWindow, listvariable=album_lv)
album_list.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
album_list.config(border=2, relief='sunken')

album_scroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=album_list.yview)
album_scroll.grid(row=1, column=1, sticky='nse', rowspan=2)
album_list['yscrollcommand'] = album_scroll.set

#       Song Listbox
song_lv = tkinter.Variable(mainWindow)
song_lv.set(("Choose a Album",))
song_list = tkinter.Listbox(mainWindow, listvariable=song_lv)
song_list.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
song_list.config(border=2, relief='sunken')

#       Main Loop
testList = range(0, 100)
album_lv.set(tuple(testList))
mainWindow.mainloop()
print("Closing db connection")
db_connection.close()
