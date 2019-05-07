"""

Name: Alexander Parker
Date: 02/02/2019
File Name: blackjack_player_hand.py
Description:  This creates the hand of the Blackjack player.
The hand class includes the cards in a player's hands.  The hand
class allows the player to view his hand and it also allows the
player to know how many points he has in his hand.

"""

class hand:

	"""
	Associate the hand with the player's name.  Be sure that
	the player_name argument for hand is player.name for each
	player's hand.
	"""

	def __init__(self, player_name):
		self.owner = player_name