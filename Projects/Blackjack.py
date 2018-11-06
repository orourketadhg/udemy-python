import random
import tkinter


def load_images(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]
    extension = 'png'

    # reads in the cards for each suit
    for suit in suits:
        # number cards
        for card in range(1, 11):
            # {cardID}_{suit}.PNG
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            # add it as an imageObject to tkinter
            image = tkinter.PhotoImage(file=name)
            # append it to card_images - card value, image,
            card_images.append((card, image,))

        # face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    # pop card off top of shuffled deck
    # pop retrieves and removes an item from a list - 0 for top of deck
    next_card = deck.pop(0)
    # add image to screen
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # return value of card
    return next_card


def deal_dealer():
    deal_card(dealerCardFrame)


def deal_player():
    PlayerScore = 0
    card_value = deal_card(playerCardFrame)[0]

    if card_value == 1 and not PlayerAce:
        card_value = 11

    PlayerScore += card_value

    if PlayerScore > 21 and PlayerAce:
        PlayerScore -= 10

    PlayerScoreLabel.set(PlayerScore)

    if PlayerScore > 21:
        result_Text.set("Dealer Wins")


mainWindow = tkinter.Tk()

mainWindow.title("Blackjack")
mainWindow.geometry("640x480")
mainWindow.configure(background='green')

# StringVar holds string variable that will be updated in the GUI if changed
result_Text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_Text).grid(row=0, column=0, columnspan=3)

cardFrame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
cardFrame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

# dealer
# IntVar like StringVar
dealerScoreLabel = tkinter.IntVar()
tkinter.Label(cardFrame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
# textvariable - changeable text variable
tkinter.Label(cardFrame, textvariable=dealerScoreLabel, background="green", fg="white").grid(row=1, column=0)

# dealer embedded frame to hold cards images
dealerCardFrame = tkinter.Frame(cardFrame, background="green")
dealerCardFrame.grid(row=0, column=1, sticky="ew", rowspan=2)

# Player
PlayerScoreLabel = tkinter.IntVar()

PlayerScore = 0
PlayerAce = False

tkinter.Label(cardFrame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(cardFrame, textvariable=PlayerScoreLabel, background="green", fg="white").grid(row=3, column=0)

# player embedded frame to hold cards images
playerCardFrame = tkinter.Frame(cardFrame, background="green")
playerCardFrame.grid(row=2, column=1, sticky="ew", rowspan=2)

# Buttons
ButtonFrame = tkinter.Frame(mainWindow)
ButtonFrame.grid(row=3, column=0, columnspan=3, sticky="w")

dealerButton = tkinter.Button(ButtonFrame, text="dealer", command=deal_dealer)
dealerButton.grid(row=0, column=0)
PlayerButton = tkinter.Button(ButtonFrame, text="player", command=deal_player)
PlayerButton.grid(row=0, column=1)

cards = []
load_images(cards)
# print(cards)

# create a new deck from cards + shuffle
deck = list(cards)
random.shuffle(deck)

dealerHand = []
playerHand = []

mainWindow.mainloop()
