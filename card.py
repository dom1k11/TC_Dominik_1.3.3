import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


    def __repr__(self):
        return f"{self.rank} of {self.suit}"  

    @staticmethod
    def create_deck():
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        deck = []

        for rank in ranks:
            for suit in suits:
                deck.append(Card(suit, rank))
        return deck
    

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):
        return f"{self.name}'s hand: {self.hand}\n"
    
deck = Card.create_deck()

random.shuffle(deck)

player1 = Player("Dominik")
player2 = Player("Bot")

player1.hand = deck[:26]
player2.hand = deck[26:]


#players' hands
print(player1) 
print(player2)

