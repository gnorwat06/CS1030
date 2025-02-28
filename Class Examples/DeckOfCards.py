#Description: pick 4 random cards out of a 52 card deck

#import random module
from random import shuffle

#Create the deck of 52 cards
deck = [x for x in range(52)]

#Create suits and rang lists
suites = ["Spades","Hearts","Diamonds","Clubs"]
ranks = ["Ace",'2','3','4','5','6','7','8','9','10',"Jack","Queen","King"]

#Shuffle our cards
shuffle(deck)

#Display four cards
for i in range(4):
    #Suit Calculation: since there are 13 cards in each suit
    #deck = 0 - 12 the results will be 0
    #deck = 13-25 the results will be 1
    suit = suites[deck[i] // 13]

    #Rank calculation: The module operation gives the remainder when
    #the card index is divided by 13, effectivly mapping the card index to
    #its rank within the suit
    rank = ranks[deck[i] % 13]

    #Display the card
    print(f"Card number: {deck[i]} is {rank} of {suit}")
