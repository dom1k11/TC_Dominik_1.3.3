import random
from card import Player, Card


def main():
    player1, player2 = create_deck()
    print(compare(player1, player2))


def compare(player1, player2):
    round_count = 0
    max_rounds = 100

    while player1.hand and player2.hand and round_count < max_rounds:
        card1 = player1.hand.pop(0)
        card2 = player2.hand.pop(0)

        print(f"Round {round_count + 1}: {player1.name}'s : {card1} vs {player2.name}'s : {card2}")

        if card1 > card2:
            print(f"{player1.name} wins this round!")
            player1.hand.append(card1)
            player1.hand.append(card2)
        elif card2 > card1:
            print(f"{player2.name} wins this round!")
            player2.hand.append(card1)
            player2.hand.append(card2)
        else:
            print("It's a tie! Both cards are equal.")

        round_count += 1

    if round_count == max_rounds:
        print("The game ended in a draw due to too many rounds.")
    elif not player1.hand:
        print(f"{player2.name} wins the game!")
    elif not player2.hand:
        print(f"{player1.name} wins the game!")



def create_deck():
    deck = Card.create_deck()

    random.shuffle(deck)

    player1 = Player("Dominik")
    player2 = Player("BOT")
    player1.hand = deck[:26]
    player2.hand = deck[26:]
    return player1, player2


def play_game():
    ...
    # TO DO implement While loop until player1/player2 out of cards


def war_scenario():
    ...
    # TO DO implement what happens if cards are matching


def play_round():

    ...
    # TO DO implement every round put cards on table from 2 tables


main()
