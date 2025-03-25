import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.rank_values = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, 
            "J": 11, "Q": 12, "K": 13, "A": 14
        }


    def __gt__(self, other):
        return self.rank_values[self.rank] > self.rank_values[other.rank]

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
    

    def compare(player1, player2):
        if player1.hand[0] > player2.hand[0]:
            print(f"{player1.name} is higher than {player2.name}")
        else:
            print(f"{player2.name} is higher than {player1.name}")
    

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):
        return f"{self.name}'s hand: {self.hand}\n"
    


