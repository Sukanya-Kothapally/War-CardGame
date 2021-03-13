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
        self.temp = [] #Storing the cards in a list when the game is tie

    ''' on each turn each card is drawn and 
        this function holds major logic'''
    def taketurn(self):
        if len(self.deck1)==0 or len(self.deck2)==0: # if any of the player has no cards the came is done
            return self.result() # created a function which displays the result of game
        open_card1=self.deck1.pop(0)
        open_card2 = self.deck2.pop(0)
        rank_card1= rank[open_card1]
        rank_card2= rank[open_card2]
        #print(open_card1+" ----- "+open_card2)
        count1, count2 = 0, 0
        print("{:12}{:12}".format(open_card1, open_card2), end='')
        # print(rank_card1,rank_card2)
        if rank_card1> rank_card2: # checking the ranks of the cards open
            print("Player 1 has the highest card and take the cards")
            self.deck1.extend([open_card1,open_card2]) # adding the cards to the deck of the player who will win for that round
            self.deck1.extend(self.temp)
            self.temp=[]
        elif rank_card1<rank_card2:
            print("Player 2 has the highest card and take the cards")
            self.deck2.extend([open_card2,open_card1])
            self.deck2.extend(self.temp)
            self.temp = []
        else:
            print("Game is Tie!! Both the cards have equal rank") # when the rank of both the cards is same
            if len(self.deck1) == 0 or len(self.deck2) == 0: # checking if any of the players are with no cards to declare the winner
                return self.result()

            open_card3=self.deck1.pop(0) # opening the next card for player1
            open_card4=self.deck2.pop(0) # opening the next card for player2
            self.temp.extend([open_card1,open_card2,open_card3,open_card4]) # adding all the cards to a list and add them to the player who wins in the next round
            print("{:12}{:12}".format("***", "***"), 'Next cards drawn should be face down.', sep='')
            return self.taketurn()
        return True

    ''' This function displays the winner based on the cards count '''
    def result(self):
        if len(self.deck1)==0:
            if len(self.deck2)==0:
                print("\nThe cards on the deck has same rank, GAME IS TIE")
            else:
                print("\nPlayer 2 wins the game")
        else:
            print("\nPlayer 1 wins the game")

if __name__ == '__main__':
    cardgame=CardGame()
    while cardgame.taketurn(): # this has to continue until the winner is declared
        continue
