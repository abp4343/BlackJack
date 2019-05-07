"""

Name: Alexander Parker
Date: 02/01/2019
File Name: blackjack_class.py
Description: This file creates the classes to be used in the BlackJack
game.  

"""

#import random class for shuffling method in deck class
import random

"""

The Player class includes the player's name, the player's running
balance.  The Player class also includes the actions that the player can take
during the game, like betting(placing an initial bet on the game), hitting
(asking for another card), and standing (holding your cards without asking for 
anymore)

"""

class player():

	#Create the player attributes: name, balance
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance

	"""

	Create the bet method.  The bet method allows the player to place a bet (less
	than or equal to their balance) on their hand.  If the player wins, they get
	to double their bet.  If the player loses, their bet is deducted from their
	balance.

	"""
	def bet(self, amount):
		if type(amount) != int:
			print("Invald Amount!")
		elif amount > self.balance:
			print("Insufficient Funds!")
		else:
			self.balance -= amount
			print("You have bet ${wager}. Your new account balance is {accbal}. Good luck!".format(wager = amount, accbal = self.balance))


"""

The Card class includes the number and suit of each card.

"""

class card():

	def __init__(self, suit, number):
		self.suit = suit
		self.number = number
		self.name = self.number + " of " + self.suit

"""

The Deck class
has the ability to create a deck of cards as well as
shuffle a deck of cards for the Blackjack game.

"""

class deck (card):

	#Declare list to store cards
	def __init__(self):
		self.list = []

	#build deck making use of card class
	def build_deck (self):

		#create list for numbers and suits in order to loop through to build deck
		number_name = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
		suit_name = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

		#loop through each number for each suit
		for number in range(13):
			for suit in range(4):
				self.list.append(card(suit_name[suit], number_name[number]))

	def shuffle_deck(self):

		#create counter variable
		count = 0

		#loop many times to ensure proper shuffling
		while (count < 10000):

			#generate two random numbers between 0 and lenth of deck list (52) , not including 52
			num1 = random.randint(0, 51)
			num2 = random.randint(0,51)

			#generate temp variable in order to swap two positions
			temp = self.list[num1]

			#swap list elements
			self.list[num1] = self.list[num2]
			self.list[num2] = temp

			#increment count
			count += 1


"""

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