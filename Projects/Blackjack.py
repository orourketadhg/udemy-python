import random
import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Blackjack")
mainWindow.geometry("640x480")

result_Text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_Text).grid(row=0, column=0, columnspan=3)

cardFrame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
cardFrame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

# dealer
dealerScoreLabel = tkinter.IntVar()
tkinter.Label(cardFrame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(cardFrame, textvariable=dealerScoreLabel, background="green", fg="white").grid(row=1, column=0)

dealerScoreFrame = tkinter.Frame(cardFrame, background="green").grid(row=0, column=1, sticky="ew", rowspan=2)

# Player
PlayerScoreLabel = tkinter.IntVar()
tkinter.Label(cardFrame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(cardFrame, textvariable=PlayerScoreLabel, background="green", fg="white").grid(row=3, column=0)

PlayerScoreFrame = tkinter.Frame(cardFrame, background="green").grid(row=2, column=1, rowspan=2)

mainWindow.mainloop()
