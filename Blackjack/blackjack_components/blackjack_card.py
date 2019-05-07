"""

Name: Alexander Parker
Date: 02/04/2019
File Name: blackjack_cards
Description: This file creates a Card class for the Blackjack
game.  The Card class includes the number and suit of each card.

"""

class card():

	def __init__(self, suit, number):
		self.suit = suit
		self.number = number
		self.name = self.number + " of " + self.suit