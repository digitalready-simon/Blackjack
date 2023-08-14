import random

class Card():

    # Constants for 13 values and 4 suits
    VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    SUITS = ["Clubs", "Spades", "Diamonds", "Hearts"]

    # Constructor
    # ex: example_card = Card(3, "Hearts")
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # TWO_OF_HEARTS = Card(2, "Hearts")
    # print(TWO_OF_HEARTS.value)

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

class BlackjackGame():
    def __init__(self):
        # Initialize the game by creating a new deck, setting player's and dealer's hands, and initializing their points.
        self.deck = Card.new_deck()  # Create a shuffled deck of cards
        self.playerHand = []         # Player's hand starts empty
        self.dealerHand = []         # Dealer's hand starts empty
        self.playerPoints = 100      # Player starts with 100 points
        self.dealerPoints = 100      # Dealer starts with 100 points

    def drawCard(self):
        # Draw a card from the deck and remove it from the deck.
        return self.deck.pop()

    def calculateHandValue(self, hand):
        # Calculate the value of a hand considering Aces as 1 or 11.
        value = sum(card.value if card.value <= 10 else 10 for card in hand)
        numAces = sum(1 for card in hand if card.value == 1)

        while numAces > 0 and value > 21:
            value -= 10
            numAces -= 1

        return value

    def playerTurn(self):
        while True:
            playerValue = self.calculateHandValue(self.playerHand)
            print(f"Player's hand: {self.playerHand} (Value: {playerValue})")

            if playerValue == 21:
                print("Player wins with 21!")
                self.playerPoints += 10   # Player wins and gains 10 points
                self.dealerPoints -= 10   # Dealer loses 10 points
                return False

            action = input("Do you want to hit or stand? ").strip().lower()

            if action == "hit":
                self.playerHand.append(self.drawCard())  # Player draws a card
                if self.calculateHandValue(self.playerHand) > 21:
                    print("Player busts! Dealer wins.")
                    self.dealerPoints += 10   # Dealer wins and gains 10 points
                    self.playerPoints -= 10   # Player loses 10 points
                    return False
            elif action == "stand":
                return True

    def play(self):
        while self.playerPoints > 0 and self.dealerPoints > 0:
            print(f"Player points: {self.playerPoints} | Dealer points: {self.dealerPoints}")
            
            # Deal initial hands
            self.playerHand = [self.drawCard(), self.drawCard()]
            self.dealerHand = [self.drawCard(), self.drawCard()]

            if self.playerTurn():
                self.dealerTurn()  # Let the dealer play their turn
                winner = self.determineWinner()  # Determine the winner of the round
                if winner == "player":
                    print("Player wins!")
                    self.playerPoints += 10   # Player wins and gains 10 points
                    self.dealerPoints -= 10   # Dealer loses 10 points
                elif winner == "dealer":
                    print("Dealer wins!")
                    self.dealerPoints += 10   # Dealer wins and gains 10 points
                    self.playerPoints -= 10   # Player loses 10 points
                else:
                    print("It's a tie!")

        if self.playerPoints <= 0:
            print("Player has run out of points. Dealer wins!")
        else:
            print("Dealer has run out of points. Player wins!")

if __name__ == "__main__":
    # Start the game
    game = BlackjackGame()
    game.play()