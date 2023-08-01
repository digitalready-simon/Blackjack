import random

# Package for a Card data structure
# Includes constructor to make new card data,
# and the static method "Card.new_deck()"
# to generate a new shuffled deck of cards
class Card():

    # Constants for 13 values and 4 suits
    VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    SUITS = ["Clubs", "Spades", "Diamonds", "Hearts"]

    # Constructor
    # ex: example_card = Card(3, "Hearts")
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # New Shuffled Deck Method
    # ex: shulffed_deck = Card.new_deck()
    def new_deck():
        deck = []
        for suit in Card.SUITS:
            for value in Card.VALUES:
                deck.append(Card(value, suit))
        random.shuffle(deck)
        return deck

    # Print a card as a string
    # ex: print(example_card) -> "♥3"
    def __repr__(self):
        # ♣ ♦ ♥ ♠
        if self.suit == "Clubs":
            symbol = "♣"
        elif self.suit == "Spades":
            symbol = "♠"
        elif self.suit == "Diamonds":
            symbol = "♦"
        elif self.suit == "Hearts":
            symbol = "♥"
        else:
            raise Exception("Invalid Suit")

        if self.value == 11:
            val = "J"
        elif self.value == 12:
            val = "Q"
        elif self.value == 13:
            val = "K"
        elif self.value == 1:
            val = "A"
        else: val = self.value

        return f"{symbol}{val}"
