"""

Name: Alexander Parker
Date: 02/04/2019
File Name: blackjack_deck
Description: This file will create a Deck class. The Deck class
has the ability to create a deck of cards as well as
shuffle a deck of cards for the Blackjack game.

"""

class deck ():

	#give deck name with initialization
	def __init__(self, name):
		self.name = name

	#build deck making use of card class
