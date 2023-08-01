# Rename this file to the name of your game and delete this comment
# Names: Simon Ha, Vinh Tran, William Liang, David Deji, Darian 
# Date: 7/26/23

# Import statements
import random
from card import Card
import user

# Program your game here!
def blackjack():
    hand = init_hand()
    game_over = False
    player = user.User()
    
# Rename this function to the name of your game and delete this comment
    deck = Card.new_deck()
    user_input = player.valid_input()
    # Deal a card
    deal = input("Hit or Stand?")
    if deal == "Hit":
        return user.hand.append(deck.pop())
    
    
    
        
    else:
        print("gameover")
        # They said no, so game ends
    print(deck)
    
# Code that runs when script is called from terminal
# ex: python my_card_game.py
if __name__ == "__main__":
    blackjack()

# To deal a card after a hit
def deal(deck):
    return deck.pop()

# Starting hand
def init_hand(deck):
    x = deal(deck)
    return list(x)