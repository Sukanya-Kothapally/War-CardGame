import math
import random

card_faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] # Card values in a deck
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades'] # Suites available in total card set
deck=[]
for i in card_faces:
    for j in suits:
        cardval= i + " " +j
        deck.append(cardval) # Appending all values available in cards to alist
#print(deck)

''' generating rank to each card to compare them'''
rank={}
for i in range(len(deck)):
    rank[deck[i]]=math.floor(i/4)
#print(rank)

class CardGame:
    def __init__(self):
        random.shuffle(deck) # Shuffling the deck
        self.deck1 = deck[26:] # splitting the cards for deck1
        self.deck2 = deck[:26] # splitting the cards for deck2

    ''' on each turn each card is drawn and 
        this function holds major logic'''

    def taketurn(self):
        if len(self.deck1)==0 or len(self.deck2)==0: # if any of the player has no cards the came is done
            return self.result() # created a function which displays the result of game
        open_card1=self.deck1.pop(0)
        open_card2 = self.deck2.pop(0)
        rank_card1= rank[open_card1]
        rank_card2= rank[open_card2]
        print(open_card1+" ----- "+open_card2)
        print(rank_card1,rank_card2)

    ''' This function displays the winner based on the cards count '''
    def result(self):
        if len(self.deck1)==0:
            if len(self.deck2)==0:
                print("\n The cards on the deck has same rank, GAME IS TIE")
            else:
                print("\n Player 2 wins the game")
        else:
            print("\n Player 1 wins the game")


if __name__ == '__main__':
    cardgame=CardGame()
    while cardgame.taketurn(): # this has to continue until the winner is declared
        continue
