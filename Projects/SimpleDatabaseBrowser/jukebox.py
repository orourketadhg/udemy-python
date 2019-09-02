#!usr/bin/env python

"""
file descriptor

"""

__author__ = "Tadhg O'Rourke"
__date__ = "02/09/2019"


import sqlite3
import tkinter

db_connection = sqlite3.connect('music.db')


class ScrollBox(tkinter.Listbox):

    """
    condensed scrollbar code for list boxes into class that subclasses listbox
    """

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nse', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


def get_albums(event):
    lb = event.widget
    index = lb.curselection()[0]
    artist_name = lb.get(index),

    # get artist ID from db
    artist_id = db_connection.execute('SELECT artists._id FROM artists WHERE artists.name = ?', artist_name).fetchone()
    alist = []

    for album in db_connection.execute('SELECT albums.name FROM albums WHERE albums.artist=? ORDER BY albums.name', artist_id):
        alist.append(album[0])

    album_lv.set(tuple(alist))

    song_lv.set(("Choose an album",))


def get_songs(event):
    lb = event.widget
    index = int(lb.curselection()[0])
    album_name = lb.get(index),

    # get artist ID from db
    album_id = db_connection.execute('SELECT albums._id FROM albums WHERE albums.name = ?', album_name).fetchone()
    alist = []

    for song in db_connection.execute('SELECT songs.title FROM songs WHERE songs.album = ? ORDER BY songs.track', album_id):
        alist.append(song[0])

    song_lv.set(tuple(alist))


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
artist_list = ScrollBox(mainWindow)
artist_list.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artist_list.config(border=2, relief='sunken')

# insert artists into artist listbox via query
for artist in db_connection.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    artist_list.insert(tkinter.END, artist[0])

artist_list.bind('<<ListboxSelect>>', get_albums)

#       Album Listbox
album_lv = tkinter.Variable(mainWindow)
album_lv.set(("Choose an Artist",))
album_list = ScrollBox(mainWindow, listvariable=album_lv)
album_list.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
album_list.config(border=2, relief='sunken')

album_list.bind('<<ListboxSelect>>', get_songs)

#       Song Listbox
song_lv = tkinter.Variable(mainWindow)
song_lv.set(("Choose a Album",))
song_list = ScrollBox(mainWindow, listvariable=song_lv)
song_list.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
song_list.config(border=2, relief='sunken')

#       Main Loop
mainWindow.mainloop()


print("Closing db connection")
db_connection.close()
