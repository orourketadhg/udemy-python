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
    # deal cards to dealer
    dealer_score = score_hand(dealerHand)
    while 0 < dealer_score < 17:
        dealerHand.append(deal_card(dealerCardFrame))
        dealerScoreLabel.set(dealer_score)
        dealer_score = score_hand(dealerHand)

    player_score = score_hand(playerHand)
    if player_score > 21:
        result_Text.set("Dealer Bust, Player Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_Text.set("Player Wins!")
    elif dealer_score > player_score:
        result_Text.set("Dealer Wins!")
    else:
        result_Text.set("Draw!")


def deal_player():
    # # changing this to a global will now update the playerScore in game
    # global PlayerScore
    # global PlayerAce
    # # player_score = 0
    # card_value = deal_card(playerCardFrame)[0]
    #
    # if card_value == 1 and not PlayerAce:
    #     card_value = 11
    #     # change the value of a global var inside a function
    #     # otherwise the global var will be converted to a local var
    #     PlayerAce = True
    #
    # # PlayerScore += card_value
    # #
    # # if PlayerScore > 21 and PlayerAce:
    # #     PlayerScore -= 10
    # #     PlayerAce = False
    #
    # PlayerScoreLabel.set(PlayerScore)
    #
    # if PlayerScore > 21:
    #     result_Text.set("Dealer Wins")
    #
    # if PlayerScore == 21:
    #     result_Text.set("Player Blackjack")
    #
    # # will print out a list of all local variables
    # print(locals())

    # Rewrite of deal_player to avoid global variables

    playerHand.append(deal_card(playerCardFrame))
    player_score = score_hand(playerHand)

    PlayerScoreLabel.set(player_score)
    if player_score > 21:
        result_Text.set("player Bust, Dealer Wins")


def score_hand(hand):
    # calculate the total score of all cards in the list
    # only one ace can have the value of 11, and this will be reduced to 1 if the hand goes bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if bust, check if there is an ace
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


mainWindow = tkinter.Tk()

mainWindow.title("Blackjack")
mainWindow.geometry("640x480")
mainWindow.configure(background='white')

# StringVar holds string variable that will be updated in the GUI if changed
result_Text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_Text).grid(row=0, column=0, columnspan=3)

cardFrame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
cardFrame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

# dealer
# IntVar like StringVar
dealerScoreLabel = tkinter.IntVar()
tkinter.Label(cardFrame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
# text-variable - changeable text variable
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

deal_player()
dealerHand.append(deal_card(dealerCardFrame))
dealerScoreLabel.set(score_hand(dealerHand))
deal_player()

mainWindow.mainloop()
