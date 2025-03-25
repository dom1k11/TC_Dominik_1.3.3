import random
from card import Player, Card

def main():
    create_deck()


def create_deck():
    deck = Card.create_deck()

    random.shuffle(deck)

    player1 = Player("Dominik")
    player2 = Player("Bot")

    player1.hand = deck[:26]
    player2.hand = deck[26:]


    #players' hands
    print(player1) 
    print(player2)

def play_game():
    ...
    #TO DO implement While loop until player1/player2 out of cards

def war_scenario():
    ...
    #TO DO implement what happens if cards are matching

def play_round():
    ...
    #TO DO implement every round put cards on table from 2 tables

main()
