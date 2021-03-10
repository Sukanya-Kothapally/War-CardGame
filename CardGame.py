import math

card_faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
deck=[]
for i in card_faces:
    for j in suits:
        deck= i + " " +j
        print(deck)
rank={}
for i in range(len(deck)):
    rank=(deck[i],math.floor(i/4))
    print(rank)

class CardGame:
    def __init__(self):
        pass

if __name__ == '__main__':
    cardgame=CardGame()
