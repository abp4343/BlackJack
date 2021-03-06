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

class Player():

	#Create the player attributes: name, balance
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance
		self.hand = []
		self.score = 0
		self.ace = False
	"""

	Create the bet method.  The bet method allows the player to place a bet (less
	than or equal to their balance) on their hand.  If the player wins, they get
	to double their bet.  If the player loses, their bet is deducted from their
	balance.

	"""
	def bet(self, amount):
		if amount <= 0:
			print("You must bet a number greater than 0.")
		elif amount > self.balance:
			print("Insufficient Funds!")
		else:
			self.balance -= amount
			print("\nYou have bet ${wager}. Your new account balance is {accbal}. Good luck!" \
				.format(wager = amount, accbal = self.balance))


"""

The Card class includes the number and suit of each card.

"""

class Card():

	def __init__(self, suit, number, value = 1):
		self.suit = suit
		self.number = number
		self.name = self.number + " of " + self.suit
		self.value = value

"""

The Deck class
has the ability to create a deck of cards as well as
shuffle a deck of cards for the Blackjack game.

"""

class Deck (Card):

	#Declare list to store cards
	def __init__(self):
		self.cards = []

	#build deck making use of card class
	def build_deck (self):

		#create list for numbers and suits in order to loop through to build deck
		number_name = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', \
		'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
		suit_name = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

		#loop through each number for each suit
		for number in range(13):
			for suit in range(4):
				if number == 0:
					self.cards.append(Card(suit_name[suit], number_name[number]))

				elif number > 0 and number < 10:
					self.cards.append(Card(suit_name[suit], number_name[number], number + 1))

				else:
					self.cards.append(Card(suit_name[suit], number_name[number], 10))


	#shuffle deck, taking advantage of builtin random class
	def shuffle_deck(self):

		#create counter variable
		count = 0

		#loop many times to ensure proper shuffling
		while (count < 10000):

			#generate two random numbers between 0 and length of deck list (52), not including 52
			num1 = random.randint(0, 51)
			num2 = random.randint(0,51)

			#generate temp variable in order to swap two positions
			temp = self.cards[num1]

			#swap list elements
			self.cards[num1] = self.cards[num2]
			self.cards[num2] = temp

			#increment count
			count += 1


"""

The hand class includes the cards in a player's hands.  The hand
class allows the player to view his hand and it also allows the
player to know how many points he has in his hand.

"""

class Hand:

	"""
	Associate the hand with the player's name.  Be sure that
	the player_name argument for hand is player.name for each
	player's hand.
	"""

	def __init__(self, player_name):
		self.owner = player_name